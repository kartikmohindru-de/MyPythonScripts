class Pardo:
    def __init__(self, cutoff_length=2, marker='x'):
        self.cutoff_length = cutoff_length
        self.marker = marker

    def __call__(self, words):
        """Process input words and classify based on length."""
        below_cutoff = []
        above_cutoff = []
        marked_strings = []

        for word in words:
            if len(word) <= self.cutoff_length:
                below_cutoff.append(word)
            else:
                above_cutoff.append(word)
                marked_strings.append(f"{self.marker}{word}{self.marker}")

        return {
            'below_cutoff': below_cutoff,
            'above_cutoff': above_cutoff,
            'marked_strings': marked_strings
        }

    def with_output(self, *args, main):
        self.output_keys = args
        self.main_key = main
        return self

    def get_outputs(self, words):
        processed = self(words)
        outputs = [processed[key] for key in self.output_keys]
        main_output = processed[self.main_key]
        return main_output, outputs


# Example usage:
process_words = Pardo  # Alias for readability

# Simulate a call
processor = process_words(cutoff_length=2, marker='x').with_output('above_cutoff', 'marked_strings', main='below_cutoff')
main_output, extra_outputs = processor.get_outputs(['a', 'an', 'apple', 'bat'])

print("Main Output (below_cutoff):", main_output)
print("Other Outputs:")
print("  above_cutoff:", extra_outputs[0])
print("  marked_strings:", extra_outputs[1])