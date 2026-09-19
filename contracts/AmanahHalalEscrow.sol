// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.24;

/// @title Sample off-chain-receipt escrow
/// @notice NOT deployed. NOT a fatwa. NOT Murabaha/Sarf. NOT a Halal authority.
/// Funds move only if a designated key signs a receipt string. That key is a project key, not JAKIM.
contract AmanahHalalEscrow {
    enum ConsignmentStatus { INEXISTENT, FUNDED, CUSTOMS_RELEASED, QUARANTINED, REJECTED, SETTLED, REFUNDED }

    struct ConsignmentEscrow {
        bytes32 consignmentId;
        address payable exporter;
        address payable importer;
        uint256 amount;
        ConsignmentStatus status;
        uint256 createdAt;
        uint256 expiryTimestamp;
    }

    address public immutable gatewaySigner;
    mapping(bytes32 => ConsignmentEscrow) public escrows;

    event EscrowFunded(bytes32 indexed consignmentId, address indexed exporter, address indexed importer, uint256 amount);
    event SettlementExecuted(bytes32 indexed consignmentId, address recipient, uint256 amount);
    event EscrowRefunded(bytes32 indexed consignmentId, address recipient, uint256 amount, string reason);

    modifier onlySigner() {
        require(msg.sender == gatewaySigner, "UNAUTHORIZED_SIGNER");
        _;
    }

    constructor(address _gatewaySigner) {
        require(_gatewaySigner != address(0), "ZERO_ADDRESS");
        gatewaySigner = _gatewaySigner;
    }

    function fundConsignmentEscrow(
        bytes32 consignmentId,
        address payable exporter,
        uint256 expiryTimestamp
    ) external payable {
        require(msg.value > 0, "ZERO_VALUE");
        require(escrows[consignmentId].status == ConsignmentStatus.INEXISTENT, "EXISTS");
        require(expiryTimestamp > block.timestamp, "EXPIRY");
        escrows[consignmentId] = ConsignmentEscrow({
            consignmentId: consignmentId,
            exporter: exporter,
            importer: payable(msg.sender),
            amount: msg.value,
            status: ConsignmentStatus.FUNDED,
            createdAt: block.timestamp,
            expiryTimestamp: expiryTimestamp
        });
        emit EscrowFunded(consignmentId, exporter, msg.sender, msg.value);
    }

    function executeCustomsSettlement(
        bytes32 consignmentId,
        bytes32 receiptHash,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) external {
        ConsignmentEscrow storage item = escrows[consignmentId];
        require(item.status == ConsignmentStatus.FUNDED, "NOT_FUNDED");
        require(block.timestamp <= item.expiryTimestamp, "EXPIRED");
        bytes32 messageHash = keccak256(abi.encodePacked(consignmentId, receiptHash, "CUSTOMS_RELEASED"));
        bytes32 ethSignedMessageHash = keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", messageHash));
        address signer = ecrecover(ethSignedMessageHash, v, r, s);
        require(signer == gatewaySigner, "BAD_SIG");
        item.status = ConsignmentStatus.SETTLED;
        (bool sent, ) = item.exporter.call{value: item.amount}("");
        require(sent, "PAY_FAIL");
        emit SettlementExecuted(consignmentId, item.exporter, item.amount);
    }

    function abortAndRefund(bytes32 consignmentId, string calldata faultReason) external onlySigner {
        ConsignmentEscrow storage item = escrows[consignmentId];
        require(item.status == ConsignmentStatus.FUNDED, "NOT_FUNDED");
        item.status = ConsignmentStatus.REFUNDED;
        (bool sent, ) = item.importer.call{value: item.amount}("");
        require(sent, "REFUND_FAIL");
        emit EscrowRefunded(consignmentId, item.importer, item.amount, faultReason);
    }
}
