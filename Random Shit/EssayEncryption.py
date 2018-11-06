def encrypt(codes, usr_str):
    encrypted_str = ''
    for ch in usr_str:
        if ch in codes:
            encrypted_str += codes[ch]
        else:
            encrypted_str += ch
    return encrypted_str

def decrypt(codes, usr_str):
    decrypted_str = ''
    keys = []
    values = []
    for key, value in codes.items():
        keys.append(key)
        values.append(value)
    for ch in usr_str:
        if ch in values:
            decrypted_str += keys[values.index(ch)]
    return decrypted_str

if __name__ == '__main__':
    codes = {'A': '1', 'a': '♫', 'B': '2', 'b': '@', 'C': '3', 'c': '#', 'D': '4', 'd': '$', 'E': '5', 'e': '%',
             'F': '6', 'f': '^', 'G': '7', 'g': '&', 'H': '8', 'h': '*', 'I': '9', 'i': '▓', 'J': '9', 'j': ')',
             'K': '[', 'k': '{', 'L': ']', 'l': '}', 'M': '≥', 'm': '|', 'N': ';', 'n': ':', 'O': "'", 'o': '♪',
             'P': ',', 'p': '<', 'Q': '.', 'q': '>', 'R': '/', 'r': '?', 'S': '`', 's': '~', 'T': '☺', 't': '▬',
             'U': '♦', 'u': '♣', 'V': '♠', 'v': '♂', 'W': '╝', 'w': '☼', 'X': '!', 'x': '(', 'Y': '±', 'y': '►', 
             'Z': '√', 'z': '⌂', ' ': 'î', '0': 'ê', '1': 'Æ', '2': '╣', '3': '¥', '4': 'µ', '5': '╠', '6': '¿',
             '7': 'ç', '8': '└', '9': '◘', '!': '§', '*': 'δ', '+': '╧', '-': 'Σ', '/': 'ⁿ', ',': 'Ü', '.': '╕',
             '?': '╫', ':': '▀', ';': '█', '"': '├', "'": '╚', '(': '¡', ')': '╔', '_': 'Ω', '[': '╜', ']': '"',
             '{': '₧', '}': '╓'}

    essay = ['Working on a farm is a great way to learn the value of hard labor. I enjoy going to my grandparents’ farm in Ottertail, Mn to help out all the time over the summer. I had gone down for the weekend to help out so my aunt and uncle were able to head to a wedding in Duluth. That left both of my grandparents, Taylor, the hired hand, and me to run the farm.',
             'Taylor, the hired hand, is a pretty chill dude. He’s got a lanky, six-foot frame with a mop of thick brown hair. He’s almost always wearing well-worn jeans with a t-shirt. It’s hard to keep jeans clean when you’re working with cattle and various machinery. He can back up anything on that farm and who knows how much else. Then there’s my grandpa, a tough weathered old man who just keeps on going. He’s got that tanned skin that’s only reached from being outside in the sun all the time. His hands are calloused and some of his fingers are crooked, whether from arthritis or some accident of his youth I don’t know. On his left wrist sits his well-worn silver watch that he always wears unless he’s sleeping or milking cows.',
             'I got down to the farm Friday afternoon after a four-hour drive. My uncle was still there at that point; however, my aunt and cousins were already in Duluth at that point. He was going to head out the next morning. Before milking that night, we hauled the last couple loads of sileage to fill the bag with. This bag is a thick, heavy, white plastic bag some couple hundred feet long that we pack the sileage into with a special machine. The sileage is made of chopped corn so it’s green and yellow and smells like cooked corn and fresh-cut grass mixed together. The machine takes the sileage from the sileage wagon and packs it in tightly with these big metal paddle like things. We finished that up and closed the bag so it could sit until we needed it.',
             'After that, it was time for milking. We milk twice a day, five-thirty in the morning, and four-thirty in the afternoon. When the milkers get turned on, it’s as loud as a pack of motorcycles going by but for two hours. I learned how to talk loud really quickly because of that and the fact that when the tractors are running the machinery it’s louder than that. Basically what happens during milking is that we corral the cows into one side of the barn so they can’t just wander and mingle with the one’s we’ve already milked. They then enter the parlor as we call it, four to a side. The parlor is made of rough concrete for the floors and a kind-of vinyl siding like material that washes clean pretty easily. The cows are standing on a floor that is about three feet higher than where we stand to milk them. Once we milk them, we let them out into the opposite side from where the other ones are being held.', 
             'The next morning, we get up and milk them at five-thirty and have breakfast at seven-thirty. Then it’s off to the field to go pull a fence line since it’s falling apart. Taylor, gramps, and I hop in the old pickup and drive there. It’s not actually that old, it’s just the oldest one they have. It’s loud and idles fast. There was one day I was driving it and idling down the driveway at twenty miles-an-hour. We get to the field and park at the approach and walk to the fence. How we did it was I would go along and pull the staples out and cut the wires every now and then when the bundles got too big while the other two wrapped the wire. Gramps would make the circle and then use the barbs to continue wrapping it around and around. Taylor had this twisting thing going on where he’d rotate it every half-circle and it would end up crisscrossing. As he said, “It doesn’t matter if it looks pretty if you’re gonna throw it out anyway.” We kept at it and got all the wire off the posts. We then went back for lunch and to feed the cows in the barn.',
             'After lunch, we headed back out there, this time however, I drove the skid loader so we could pull the posts out with its tree-puller attachment. It looks like big metal alligator teeth laid on their side with a metal grill behind it so nothing hits the cab while you’re pulling things. We drive the pickup into the ditch so as I pulled the posts, Taylor could stack them into the bed of the truck. Once we finished the edge, the bed of the pickup was stacked higher than the roof of the cab with these posts. We drove over to the brush pile by the edge of the field so we could get rid of them. But we didn’t notice that the grass around the pile was full to the brim with sandburs. So we took the skid loader and used it to tear up the ground a little bit to get rid of them so we could unload without getting covered. By that point it was getting to milking time again and so we drove the truck and skid loader back to the farm.',
             'The next day I headed back to Duluth so I wouldn’t miss any school. That was one of the best weekends of my summer because it was just me and family working. And that, is what it’s like to work on the farm for the weekend.']

    new_essay = []
    for line in essay:
        new_line = encrypt(codes, line)
        new_essay.append(new_line)
        print(new_essay[new_essay.index(new_line)])