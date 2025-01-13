# Pricing EU call option price by using Monte Carlo method
1. Set the European call option price based on the BSM model as the theoretical price.
  
$$V = S_0 N(d_1) - Ke^{-rT} N(d_2),\space where\space \space d_1 = \frac{\ln\left(\frac{S_0}{S}\right) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}, d_2 = d_1 - \sigma \sqrt{T} $$
  
2. Simulate option price by Monte Carlo method.    
3. Compare them.

# Pricing EU call option price by using finite difference method
1. Set the European call option price based on the BSM model as the theoretical price.
     
$$V = S_0 N(d_1) - Ke^{-rT} N(d_2),\space where \space \space d_1 = \frac{\ln\left(\frac{S_0}{S}\right) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}, d_2 = d_1 - \sigma \sqrt{T} $$
  
2. the BSM partial equation of EU call option is:
    
$$\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0$$  

3. the implicit finite difference form can be expressed as:  
  
$$\frac{V_i^{n+1} - V_i^n}{\Delta t} + \frac{1}{2} \sigma^2 S_i^2 \frac{V_{i+1}^{n+1} - 2V_i^{n+1} + V_{i-1}^{n+1}}{\Delta S^2} + r S_i \frac{V_{i+1}^{n+1} - V_{i-1}^{n+1}}{2\Delta S} - r V_i^{n+1} = 0$$    
  
which is:  

$$\alpha_i V_{i-1}^{n+1} + \beta_i V_i^{n+1} + \gamma_i V_{i+1}^{n+1} = V_i^n$$  
  
where,  

$$\alpha_i = \frac{\Delta t}{2} \left( \frac{\sigma^2 S_i^2}{\Delta S^2} - \frac{r S_i}{\Delta S} \right)$$  
  
$$\beta_i = 1-\Delta t \left( \frac{\sigma^2 S_i^2}{\Delta S^2} + r \right)$$  
  
$$\gamma_i = \frac{\Delta t}{2} \left( \frac{\sigma^2 S_i^2}{\Delta S^2} + \frac{r S_i}{\Delta S} \right)$$  

3. Simulate option price by implicit finite difference method.
4. Compare them




