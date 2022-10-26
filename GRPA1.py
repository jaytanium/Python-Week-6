def get_toppers(scores_dataset, subject, gender):
    score = []
    name = []
    for i in range(len(scores_dataset)):
        if(scores_dataset[i]['Gender']==gender):
            score.append(scores_dataset[i][subject])
    max_score=max(score)
    for i in range(len(scores_dataset)):
        if(scores_dataset[i]['Gender']==gender):
            if(scores_dataset[i][subject]==max_score):
                name.append(scores_dataset[i]['Name'])
                

    return name
