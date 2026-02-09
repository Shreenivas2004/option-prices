
This is an simple python package to calculate greeks like theta,vega,gamma,delta and rho as well as to calculate option prices using binomial tree method and black scholes method.

# Dependencies

`Numpy` 

`Scipy`

# How to install 

`pip install option-pricings`

# How to import 
`import option_pricings`

Or import specific modules

`from option_pricings import bsm` for black scholes

`from option_pricings import binomial` for binomial tree

`from option_pricings import greeks` for greeks 

# using the package 

| Symbol | Meaning | Note |
| :--- | :--- | :--- |
| S | Spot Price | |
| K | Strike Price | |
| T | Time to Maturity | |
| r | Interest Rate | To be entered in the scale of 1-100 |
| sigma | Volatility | To be entered in the scale of 1-100 |
| u | Up Factor | |
| d | Down Factor | |

## black scholes
`from option_pricings import bsm`

`price = bsm(S=50,K=40,T=1,r=6,sigma=25,option_type="call")`

`print(price)`

The option type can be either call or put

## binomial
`from option_pricings import binomial`

`price = binomial(S=50,K=52,r=5,T=2,u=1.2,d=0.8,option_type="put",n_steps=2)`

`print(price)`

you can give either u and d or sigma and the u and d will be calculated based on that similarly you can give either time_step or n_step and the other will be calculated like wise
Note: 
## greeks
`from option_pricings import greeks`

first you need to instantiate the classs

`price = greeks(S=50, K=40, T=1, r=6, sigma=25, option_type='call')`

then specify which greek you want to calculate

`greeks.delta()`

`greeks.gamma()`

`greeks.vega()`

`greeks.theta()`

`greeks.rho()`

there also an option which will calculate all the options in one go

`greeks.all()`

## Author

Shreenivas Dani

Emai: shreenivasdani@gmail.com


 


