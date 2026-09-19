pragma circom 2.1.6;

include "circomlib/circuits/poseidon.circom";
include "circomlib/circuits/comparators.circom";

// Spec-only Merkle membership circuit. Not compiled, not trusted setup, not a recipe leak-proof in production.
template HalalIngredientWhitelist(levels) {
    signal input root;
    signal input ingredientId;
    signal input salt;
    signal input pathElements[levels];
    signal input pathIndices[levels];

    signal output isValid;

    component leafHasher = Poseidon(2);
    leafHasher.inputs[0] <== ingredientId;
    leafHasher.inputs[1] <== salt;
    signal leaf <== leafHasher.out;

    signal currentHash[levels + 1];
    currentHash[0] <== leaf;

    component hashers[levels];

    for (var i = 0; i < levels; i++) {
        pathIndices[i] * (1 - pathIndices[i]) === 0;

        hashers[i] = Poseidon(2);
        signal left <== currentHash[i] + pathIndices[i] * (pathElements[i] - currentHash[i]);
        signal right <== pathElements[i] + pathIndices[i] * (currentHash[i] - pathElements[i]);
        hashers[i].inputs[0] <== left;
        hashers[i].inputs[1] <== right;
        currentHash[i + 1] <== hashers[i].out;
    }

    component equality = IsEqual();
    equality.in[0] <== currentHash[levels];
    equality.in[1] <== root;
    isValid <== equality.out;
    isValid === 1;
}

component main {public [root]} = HalalIngredientWhitelist(16);
