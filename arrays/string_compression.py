
class Solution:
  def compress(self, chars: List[str]) -> int:
    
    curr = chars[0]
    count_consec = 1
    res = []
    for i in range(1, len(chars)):
        if chars[i] == curr:
            count_consec += 1
    
        else:
            res.append(curr + str(count_consec))
            curr = chars[i]
            count_consec = 1
    
    res.append(chars[i] + str(count_consec))
            
    
    return "".join(res)
