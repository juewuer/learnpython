class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or not str:
            return s
        lens = len(s)
        ns = [""]*lens
        m=numRows-1
        cur = 0

        for i in range(0,numRows):
            for k in range(i,lens,2*m):
                ns[cur]=s[k]
                cur +=1
                if i%m!=0:
                    ne = k+m*2-2*i
                    if ne < lens:
                        ns[cur]=s[ne]
                        cur +=1
                #print(f'{i=},{k=},{s[k]=} {ne}', f'{s[ne]=}' if ne < lens and ne%m!=0 else "" )


        return ''.join(ns)


import pytest
@pytest.mark.parametrize("s,numRows,expect",[
    ("LEETCODEISHIRING",3,'LCIRETOESIIGEDHN'),
    ("LEETCODEISHIRING",4,'LDREOEIIECIHNTSG'),
    ("",1,""),
    ("abc",1,"abc"),
])
def test_solution(s, numRows, expect):
    solution = Solution()
    mock = 0
    mock_out=''
    out = expect if not mock else mock_out
    assert solution.convert(s, numRows) == out

if __name__=="__main__":
    solution = Solution()
    mock = 0
    mock_out=''

    s = ""
    numRows = 1
    #s = "0123456789abcdefghijk"
    #numRows = 6
    out = "" if not mock else mock_out
    assert solution.convert(s, numRows) == out


