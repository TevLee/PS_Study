# 14:18 - 14:37
def solution(skill, skill_trees):
    answer = 0 #가능한 스킬트리개수
    skill_list = list(skill)
    for tree in skill_trees:
        tmp = []
        for s in tree:
            if s in skill_list:
                tmp.append(s)
        for i in range(len(tmp)):
            if tmp[i] != skill_list[i]:
                break
        else :
            answer+=1
    return answer