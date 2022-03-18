function fibonacci(end) {
    let x = 0;
    let n = 0;
    let sequence = [1];

    for (let i=1; i < end; i++) {
        sequence.push(x+n);

        n = sequence[sequence.length-1];
        x = sequence[sequence.length-2];

        // n should be equal to the current sum, and x being the one preceding it
    }

    return sequence
}

console.log(fibonacci(10)); // Should return and print the first 10 fibonacci numbers
