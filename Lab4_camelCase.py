def camel_case(sentence):

    if sentence.isnumeric(): #if statment handling empty and numeric number
        return 'enter only words'
    elif sentence=="":
        return 'please enter your input'
    else:
        split_sentence=sentence.split() #for loop handling the camel case.
        cap_sentence=[split_sentence[0].lower()]
        for x in range (1, len(split_sentence)):
            cap_sentence.append(split_sentence[x].capitalize())
    return ''.join(cap_sentence)

        


def main():
    sentence=input("enter your sentence")
    camelCase=camel_case(sentence)
    print(camelCase)
if __name__ == "__main__":
    main()
