from typing import Dict, List, Tuple
from collections import Counter


def init_vocabulary() -> Dict[bytes, int]:

    end_of_text_token = "<|endoftext|>"
    vocab = {bytes([i]): i for i in range(256)}
    vocab[end_of_text_token.encode("utf-8")] = 256
    return vocab


def pretokenize(corpus: str, split: str = " ") -> Dict[Tuple[bytes], int]:

    string_pretokens = [tuple(w) for w in corpus.split(split)]

    return dict(Counter(string_pretokens))


def count_pairs(pretoken: Tuple[bytes]):

    pairs = {}

    for c, n in zip(pretoken, pretoken[1:]):

        pair = c + n

        if pair not in pairs:
            pairs[pair] = 1
        else:
            pairs[pair] += 1

    return pairs


def pair_count(pretokens: Dict[Tuple[bytes], int]):

    pairs = {}

    for pretoken, count in pretokens.items():

        pair_dict = count_pairs(pretoken)

        for p, c in pair_dict.items():

            if p in pairs:
                pairs[p] += c * count
            else:
                pairs[p] = c * count

    return dict(sorted(pairs.items(), key=lambda item: item[1], reverse=True))


def frequent_pair(pair_count: Dict[str, int]):
    return max(pair_count.items(), key=lambda item: (item[1], item[0]))[0]


def apply_merge(pretoken: Tuple[str], freq: str):

    pt = []
    # TODO

    return tuple(pt)


def merge(pretokens: Dict[Tuple[bytes], int], freq: str):

    new_pretokens = {}

    for pretoken, count in pretokens.items():

        merged = apply_merge(pretoken, freq)

        new_pretokens[merged] = count

    return new_pretokens


def main():

    corpus = "low low low low low lower lower widest widest widest newest newest newest newest newest newest"

    vocabulary = init_vocabulary()

    pretokens = pretokenize(corpus=corpus)

    for i in range(5):

        pairs = pair_count(pretokens)

        the_most_frequent_pair = frequent_pair(pairs)

        pretokens = merge(pretokens, the_most_frequent_pair)

        print(pretokens, the_most_frequent_pair)
        print()


if __name__ == "__main__":
    main()
