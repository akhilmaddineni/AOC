"""
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""

ans  = 0 
with open("input_p1.txt",'r') as f : 
    b_map = {'X' : 'A',
             'Y' : 'B',
             'Z' : 'C'}
    val_map = {
        'A' : 1,
        'B' : 2,
        'C' : 3
    }
    for line in f : 
        choice_a,choice_b =map(str,line.rstrip().split())
        if choice_b == "Y" : 
            ans += val_map[choice_a]+3
        elif choice_b == "X" : 
            if choice_a == "A" : 
                ans += val_map['C']
            elif choice_a == 'B' :
                ans += val_map['A']
            else : 
                ans += val_map['B']
        else : 
            if choice_a == "A" : 
                ans += val_map['B']+6
            elif choice_a == 'B' :
                ans += val_map['C']+6
            else : 
                ans += val_map['A']+6
        
print(ans)
             
