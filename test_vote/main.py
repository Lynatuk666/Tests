def vote(votes):
	return max(votes, key = votes.count)

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,3,2]))