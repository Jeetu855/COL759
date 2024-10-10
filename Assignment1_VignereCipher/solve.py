# import os


##if __name__=="__main__":
## def choice_Of_operation(choice):
##plaintext_to_cipher():
##def index_of_coincidence():
##def ciphertext_to_plaintext():
dis = []
diff = []
user_str = ""
Sub1 = ""
Sub2 = ""
Sub3 = ""
Sub4 = ""
Sub5 = ""
Sub_arr = []


def choice_Of_operation(choice):
    match choice:
        case 1:
            plaintext_to_ciphertext()
        case 2:
            ciphertext_to_plaintext()

        case 3:
            print("Cryptanalysis Complete,Thank you")


def plaintext_to_ciphertext():
    print(
        "To convert Plaintext to cipher text you need to give Plaintext as well as their key :"
    )
    str = input("Enter Your Plaintext :")
    str = str.upper()
    key = input("Enter your key : ")
    key = key.upper()
    str_length = len(str)
    key_length = len(key)
    cipher = ""
    i = 0  # iterate over plaintext
    v = 0  # iterate over key
    for i in range(0, str_length):
        if str[i] >= "A" and str[i] <= "Z":
            l = ord(str[i]) - 65  # get ascii value of the plaintext and then its index
            m = ord(key[(v) % key_length]) - 65  # index of key
            c = chr((l + m) % 26 + 65)  # cipher character
            cipher += c
            v += 1
        else:  # if any other char
            cipher += str[i]
    print("Your Plaintext :", str)
    print("Your Ciphertext :", cipher)
    # input()  ##for hold comsole window
    # os.system("cls")  ##clear console window


def index_of_coincidence(str):
    str = str.upper()
    print(f"In the sequence \n{str}\n")
    freq_table = []  ##to store Alphabet , frequency,frequency-1,(frequency*frequency-1)
    freq_count = 0  ## total valid letters n
    freq_total = 0  ## sum of all ni*ni-1
    for i in range(0, 26):
        V = []
        ch = chr(65 + i)
        n = str.count(ch)
        n1 = n - 1
        total = n * n1
        V.append(ch)
        V.append(n)
        V.append(n1)
        V.append(total)
        freq_table.append(V)
        freq_count = freq_count + n  ## total valid letters n
        freq_total = freq_total + total  ## sum of all ni*ni-1
    V = []
    V.append("Total")
    V.append(freq_count)  ## append total freqency of character ,and ni*n-1 into list
    V.append("Null")
    V.append(freq_total)
    freq_table.append(V)
    # for i in freq_table:
    #    print(i)
    IC1 = freq_total / freq_count  ### calculating index of coincidence
    IC = IC1 / (freq_count - 1)
    return IC


def generate_subsequence():
    global user_str
    global Sub_arr
    global answer
    print("in subsequence")

    sub2_1 = user_str[::2]
    sub2_2 = user_str[1::2]
    sub3_1 = user_str[::3]
    sub3_2 = user_str[1::3]
    sub3_3 = user_str[2::3]
    sub4_1 = user_str[::4]
    sub4_2 = user_str[1::4]
    sub4_3 = user_str[2::4]
    sub4_4 = user_str[3::4]
    sub5_1 = user_str[::5]
    sub5_2 = user_str[1::5]
    sub5_3 = user_str[2::5]
    sub5_4 = user_str[3::5]
    sub5_5 = user_str[4::5]

    IC_sub2_1 = index_of_coincidence(sub2_1)
    IC_sub2_2 = index_of_coincidence(sub2_2)
    IC_sub3_1 = index_of_coincidence(sub3_1)
    IC_sub3_2 = index_of_coincidence(sub3_2)
    IC_sub3_3 = index_of_coincidence(sub3_3)
    IC_sub4_1 = index_of_coincidence(sub4_1)
    IC_sub4_2 = index_of_coincidence(sub4_2)
    IC_sub4_3 = index_of_coincidence(sub4_3)
    IC_sub4_4 = index_of_coincidence(sub4_4)
    IC_sub5_1 = index_of_coincidence(sub5_1)
    IC_sub5_2 = index_of_coincidence(sub5_2)
    IC_sub5_3 = index_of_coincidence(sub5_3)
    IC_sub5_4 = index_of_coincidence(sub5_4)
    IC_sub5_5 = index_of_coincidence(sub5_5)

    IC_2 = (IC_sub2_1 + IC_sub2_2) / 2
    IC_3 = (IC_sub3_1 + IC_sub3_2 + IC_sub3_3) / 3
    IC_4 = (IC_sub4_4 + IC_sub4_3 + IC_sub4_2 + IC_sub4_1) / 4
    IC_5 = (IC_sub5_5 + IC_sub5_4 + IC_sub5_3 + IC_sub5_2 + IC_sub5_1) / 5
    print(f"IC_sub2_1: {IC_sub2_1}\nIC_sub2_2: {IC_sub2_2}\n")
    print(f"IC_sub3_1: {IC_sub3_1}\nIC_sub3_2: {IC_sub3_2}\nIC_sub3_3: {IC_sub3_3}\n")
    print(
        f"IC_sub4_1: {IC_sub4_1}\nIC_sub4_2: {IC_sub4_2}\nIC_sub4_3: {IC_sub4_3}\nIC_sub4_4: {IC_sub4_4}\n"
    )
    print(
        f"IC_sub5_1: {IC_sub5_1}\nIC_sub5_2: {IC_sub5_2}\nIC_sub5_3: {IC_sub5_3}\nIC_sub5_4: {IC_sub5_4}\nIC_sub5_5: {IC_sub5_5}\n"
    )

    print(f"IC 2 is {IC_2}\n")
    print(f"IC 3 is {IC_3}\n")
    print(f"IC 4 is {IC_4}\n")
    print(f"IC 5 is {IC_5}\n")

    abs_IC_2 = abs(IC_2 - 0.068)
    abs_IC_3 = abs(IC_3 - 0.068)
    abs_IC_4 = abs(IC_4 - 0.068)
    abs_IC_5 = abs(IC_5 - 0.068)

    # Print the absolute differences for debugging
    print(f"abs_IC_2: {abs_IC_2}")
    print(f"abs_IC_3: {abs_IC_3}")
    print(f"abs_IC_4: {abs_IC_4}")
    print(f"abs_IC_5: {abs_IC_5}")

    # Determine the smallest absolute difference and update Sub_arr
    if abs_IC_2 <= abs_IC_3 and abs_IC_2 <= abs_IC_4 and abs_IC_2 <= abs_IC_5:
        Sub_arr.extend([sub2_1, sub2_2])
        print("IC_2 is the smallest")
    elif abs_IC_3 <= abs_IC_2 and abs_IC_3 <= abs_IC_4 and abs_IC_3 <= abs_IC_5:
        Sub_arr.extend([sub3_1, sub3_2, sub3_3])
        print("IC_3 is the smallest")
    elif abs_IC_4 <= abs_IC_2 and abs_IC_4 <= abs_IC_3 and abs_IC_4 <= abs_IC_5:
        Sub_arr.extend([sub4_1, sub4_2, sub4_3, sub4_4])
        print("IC_4 is the smallest")
    else:
        Sub_arr.extend([sub5_1, sub5_2, sub5_3, sub5_4, sub5_5])
        print("IC_5 is the smallest")

    # for string in Sub_arr:
    result = []
    #   print(string)
    print(f"**********{len(Sub_arr)}")
    for sub in Sub_arr:
        frequency_count = {}
        print(sub)
        # Count the frequency of each character in the subsequence
        for char in sub:
            if char in frequency_count:
                frequency_count[char] += 1
            else:
                frequency_count[char] = 1

        # Find the character with the highest frequency
        max_frequency = 0
        most_frequent_char = ""

        for char, count in frequency_count.items():
            if count > max_frequency:
                max_frequency = count
                most_frequent_char = char

        # Append the result (most frequent character)
    result.append(most_frequent_char)

    print(result)
    base_char = "E"

    answer = []
    for char in result:
        # Compute the shift of the character with respect to 'E' mod 26
        shift = (ord(char) - ord(base_char)) % 26

        # Compute the character corresponding to the shift
        shift_char = chr(ord("A") + shift)

        # Print the character
        print(shift_char)
        answer.append(shift_char)

    print(f"************{answer}**************")
    answer.clear()


def ciphertext_to_plaintext():
    global user_str
    print("To convert Ciphertext to plaintext you need to give cipher text")
    user_input = input(
        "Enter Your cipher text :"
    )  # Store the user input in a separate variable
    user_str = "".join(
        filter(str.isalpha, user_input)
    ).upper()  # Clean and set user_str
    generate_subsequence()  # Generate subsequences based on cleaned user_str


def freq_of_factor_length_of_key():
    # distance between subsequence and the most common factors
    global dis
    global diff
    str = input("Enter cipher text")
    frequency = []
    for i in range(2, 20):
        frequency.append([i, 0])

    def position(substr):
        index = 0
        d = []  ##hold position of substring only
        d1 = []  ##difference between two string
        d1.append(substr)
        d.append(substr)
        for i in range(str.count(substr)):
            index = str.find(substr, index)
            d.append(index)
            index = index + len(substr)
        dis.append(d)
        l = len(d)
        i = 1
        while i < l - 1:
            j = i + 1
            while j < l:
                d1.append(d[j] - d[i])
                j = j + 1
            i = i + 1
        diff.append(d1)

    # arr1 = []      ##contain frequency of singe letter
    # for i in range(26):
    #         substr = "" + chr(i + 65)  + ""     # X
    #         if str.count(substr) > 1:
    #             arr1.insert(0, ( str.count(substr), substr))

    # arr1.sort(reverse=True)
    # print("Frequency Of Single Character in Cypertext:\n",arr1)

    arr2 = []  ##contain frequency of digraphs
    for i in range(26):
        for j in range(26):
            substr = "" + chr(i + 65) + chr(j + 65) + ""  # XY
            if str.count(substr) > 1:
                arr2.insert(0, (str.count(substr), substr))
                position(substr)

    arr2.sort(reverse=True)
    print("\n\nFrequency Of digraphs in Cypertext:\n", arr2)

    arr3 = []  ##contain frequency of trigraph
    for i in range(26):
        for j in range(26):
            for k in range(26):
                substr = "" + chr(i + 65) + chr(j + 65) + chr(k + 65) + ""  # XYZ
                if str.count(substr) > 1:
                    arr3.insert(0, (str.count(substr), substr))
                    position(substr)
    arr3.sort(reverse=True)
    print("\n\nFrequency Of trigraph 3 letter  in Cypertext:\n", arr3)
    arr4 = []  ##contain frequency of 4 length word
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    substr = (
                        "" + chr(i + 65) + chr(j + 65) + chr(k + 65) + chr(l + 65) + ""
                    )  # ABCD
                    if str.count(substr) > 1:
                        arr4.insert(0, (str.count(substr), substr))
                        position(substr)

    arr4.sort(reverse=True)
    print("\n\nFrequency Of 4 letter word in Cypertext:\n", arr4)

    # arr5=[]     ##contain frequency of 5 letter word
    # for i in range(26):
    #     for j in range(26):
    #         for k in range(26):
    #             for l in range(26):
    #                 for m in range(26):
    #                     substr = "" + chr(i + 65) + chr(j + 65) + chr(k + 65) +chr(l+65)+chr(m+65)+ ""  #ABCDE
    #                     if str.count(substr) >1:
    #                        arr5.insert(0, ( str.count(substr), substr ))

    # arr5.sort(reverse=True)
    # print("\n\nFrequency Of 5 letter word in Cypertext:\n",arr5)
    print("dis = ", dis)
    print("diff", diff)
    for i in diff:
        j = 1
        while j < len(i):
            for k in range(2, 20):
                if i[j] % k == 0:
                    frequency[k - 2][1] += 1
            j = j + 1
    print("frequency of factor:", frequency)


if __name__ == "__main__":
    choice = None
    while choice != 3:
        print("1.From Plaintext to Ciphertext")
        print("2. From Ciphertext to Plaintext")
        print("3. for exit")
        choice = int(input("Please Enter input Choice[1,2,3]:"))
        choice_Of_operation(choice)
