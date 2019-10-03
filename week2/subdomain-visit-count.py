import collections
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # split cpdomains into num and domains
        r = []
        c = collections.Counter()
        for s in cpdomains:
            num, domain = s.split()
            num = int(num)
            subs = domain.split('.')
            for i in range(len(subs)):
                c['.'.join(subs[i:])] += num
                
        return [str(c[x]) + ' ' + x for x in c]