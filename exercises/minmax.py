def find_max_min(lists):
  mins = lists[0]
  maxs = lists[0]
  
  for i in lists:
    if maxs < i:
      maxs = i
    if mins > i:
      mins = i
      
  if maxs == mins:
    return [len(lists)]
      
  return [mins,maxs]
      