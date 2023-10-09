#!/usr/bin/python3
import pathlib

import openai
import argparse


def anfrage(program, req, answer):
    openai.organization = "ORGKey"
    openai.api_key = "APIKEY"

    completion1 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.2,
        messages=[
            {"role": "system", "content": "You are a software verifier."},
            {"role": "user", "content": req + '\n' + open(program, 'r').read()},

        ]
    )
    print(completion1.choices[0])

    completion2 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.2,
        messages=[
            {"role": "system", "content": "You are a software verifier."},
            {"role": "user", "content": req + '\n' + open(program, 'r').read()},
            completion1.choices[0].message,
            {"role": "user", "content": answer}
        ]
    )
    print(completion2.choices[0])

    response = str(completion2.choices[0].message)
    res = response.lower()
    answer = "Error"

    if "yes" in res or "no" in res or "unknown" in res:
        for x in range(len(res)):
            if res[x] == "y":
                if x == 0 and x + 3 == len(res) and res[x + 1] == "e" and res[x + 2] == "s":
                    answer = "Yes"
                    break
                elif x > 0 and x + 3 == len(res) and res[x + 1] == "e" and res[x + 2] == "s":
                    answer = "Yes"
                    break
                elif x + 3 < len(res):
                    if res[x + 1] == "e" and res[x + 2] == "s" and (
                            res[x + 3] == '"' or res[x + 3].isspace() or res[x + 3] == "." or res[x + 3] == ","):
                        answer = "Yes"
                        break
                else:
                    continue
            elif res[x] == "n":
                if x == 0 and x + 2 == len(res) and res[x + 1] == "o":
                    answer = "No"
                    break
                elif x > 0 and x + 2 == len(res) and res[x + 1] == "o":
                    answer = "No"
                    break
                elif x + 2 < len(res):
                    if res[x + 1] == "o" and (
                            res[x + 2] == '"' or res[x + 2].isspace() or res[x + 2] == "." or res[x + 2] == ","):
                        answer = "No"
                        break
                else:
                    continue
            elif res[x] == "u":
                if x == 0 and x + 7 == len(res) and res[x + 1] == "n" and res[x + 2] == "k" and res[
                    x + 3] == "n" and \
                        res[
                            x + 4] == "o" and res[x + 5] == "w" and res[x + 6] == "n":
                    answer = "Unknown"
                    break
                elif x > 0 and x + 7 == len(res) and res[x + 1] == "n" and res[x + 2] == "k" and res[
                    x + 3] == "n" and \
                        res[
                            x + 4] == "o" and res[x + 5] == "w" and res[x + 6] == "n":
                    answer = "Unknown"
                    break
                elif x + 7 < len(res):
                    if res[x + 1] == "n" and res[x + 2] == "k" and res[x + 3] == "n" and res[x + 4] == "o" and res[
                        x + 5] == "w" and res[x + 6] == "n" and (
                            res[x + 7] == '"' or res[x + 7] == " " or res[x + 7] == "." or res[x + 7] == ","):
                        answer = "Unknown"
                        break
                else:
                    continue

    print(answer)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Executes ChatGPT')

    parser.add_argument('program', type=str, help='enter file path')
    parser.add_argument('--test', type=int, help='<Required> Enter 1 - 4', choices={1, 2, 3, 4}, required=True)
    parser.add_argument('--32', action='store_true')
    parser.add_argument('--64', action='store_true')
    args = parser.parse_args()
    coolerPfad = args.program

    if args.test == 1:
        anfrage(coolerPfad, "Does this program pass all assertions?", "Answer with "
                                                                                                        "yes, no or"
                                                                                                        "unknown to the"
                                                                                                        "question. If you think, "
                                                                                                        "all assertions are"
                                                                                                        "passed answer with 'Yes'. "
                                                                                                        "If you dont think"
                                                                                                        "all assertions are passed "
                                                                                                        "answer with 'No'. If"
                                                                                                        "you are unsure answer "
                                                                                                        "with 'Unknown'.")
    elif args.test == 2:
        print("2")
    else:
        print("Error")
