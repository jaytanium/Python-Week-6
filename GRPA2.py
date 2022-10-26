def freq_to_words(words):
    word_set=set(words)
    d={}
    for i in word_set:
      count=0
      for j in range(len(words)):
          if(words[j]==i):
             count=count+1
      if(count in d):
          d[count].append(i)
      else:
          d[count]=[i]
    return d
           
