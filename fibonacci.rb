def fibonacci(sequence_end)
    x,n,sequence = 0,1,[1]
    
    for _ in 0..sequence_end
        sequence.push(x+n)

        n,x = sequence[-1], sequence[-2]
    end

    return sequence
end

p fibonacci(10) # Should return and print the first 10 fibonacci numbers
