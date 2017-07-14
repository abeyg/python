# Write your list_stats function here.
def list_stats(d):
  d.sort()
  mean=0
  med=0
  sz=len(d)
  if sz % 2 == 0:
    med = (d[sz//2]+d[sz//2-1])/2
  else:
    med = d[sz//2]
  mean = sum(d)/sz
  return (med, mean)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)
