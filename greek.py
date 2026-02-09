import numpy as np
from scipy.stats import norm

class greeks:
   
    def __init__(self, S, K, T, r, sigma, option_type='call'):
        self.S = S
        self.K = K
        self.T = T
        self.r = r/100
        self.sigma = sigma/100
        self.type = option_type.lower()

    # Internal helper 
    def _d1_d2(self):
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return d1, d2
    
    # User-facing methods
    def delta(self):
        d1, _ = self._d1_d2()
        if self.type == 'call':
            res= norm.cdf(d1)
            return res.round(2)
        res =norm.cdf(d1) - 1
        return res.round(4)

    def gamma(self):
        d1, _ = self._d1_d2()
        return (norm.pdf(d1) / (self.S * self.sigma * np.sqrt(self.T))).round(2)


    def vega(self):
        d1, _ = self._d1_d2()
        return (self.S * norm.pdf(d1) * np.sqrt(self.T) / 100).round(4)

    def theta(self):
        d1, d2 = self._d1_d2()
        term1 = -(self.S * norm.pdf(d1) * self.sigma) / (2 * np.sqrt(self.T))

        if self.type == 'call':
            term2 = self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
            theta = term1 - term2
        else:
            term2 = self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-d2)
            theta = term1 + term2

        return (theta / 365).round(4)
            
    def rho(self):
        _, d2 = self._d1_d2()

        if self.type == 'call':
            rho = self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(d2)
        else:
            rho = -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-d2)

        return (rho / 100).round(4)



    # Ek "Master Function" jo sab return kare (User convenience ke liye)
    def all(self):
        all = {
            "delta": float(self.delta()),
            "gamma": float(self.gamma()),
            "vega": float(self.vega()),
            "theta": float(self.theta()),
            "rho": float(self.rho())
            # baaki greeks bhi add kar lena
        }
        return all
    



