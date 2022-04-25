ref_f = open('C:/Users/User/Desktop/개인문서/새 폴더/ref.txt', 'r')
src_f = open('C:/Users/User/Desktop/개인문서/새 폴더/src.txt', 'r')

save_f = open('C:/Users/User/Desktop/개인문서/새 폴더/save.txt', 'w')
save_t = ''

src_line = src_f.readline()
src = src_line.strip()

ans = []

while True:
    
    Pre_line = ref_f.readline()
    Seq_line = ref_f.readline()
    src_string = ''
    
    if Pre_line == "" and Seq_line == "": 
        break
    
    if src in Seq_line:
        pos = Seq_line.find(src)
        
        for idx, c in enumerate(Seq_line[pos:]):
            if len(src) > idx:
                src_string += c
        
        LocA = pos + 1
        LocB = len(src_string) + pos
        ans.append((Pre_line.strip(), LocA, LocB, src_string))
        save_t += Pre_line.strip() + "\t" +str(LocA) + '-' + str(LocB) + '\n' + src_string+'\n'
#        ans.append((Pre_line, src_string, LocA, LocB))

print(ans)
save_f.write(save_t)
save_f.close()        
