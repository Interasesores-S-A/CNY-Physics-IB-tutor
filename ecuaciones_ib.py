# Base de ecuaciones del IB Physics Data Booklet
# Optimizada para uso con IA, Python y graficación

ecuaciones_ib = {

# --------------------------------
# A. Space, time and motion
# --------------------------------

"A1_kinematics": [

{
    "eq": "v = u + a*t",
    "variables": ["v","u","a","t"],
    "graficable": True
},

{
    "eq": "s = u*t + 0.5*a*t**2",
    "variables": ["s","u","a","t"],
    "graficable": True
},

{
    "eq": "v**2 = u**2 + 2*a*s",
    "variables": ["v","u","a","s"],
    "graficable": False
},

{
    "eq": "s = (u + v)*t/2",
    "variables": ["s","u","v","t"],
    "graficable": True
}

],

# --------------------------------

"A2_forces_momentum": [

{"eq":"F_f <= mu*N","variables":["F_f","mu","N"],"graficable":False},
{"eq":"F_f = mu*N","variables":["F_f","mu","N"],"graficable":True},
{"eq":"F = -k*x","variables":["F","k","x"],"graficable":True},
{"eq":"F_d = 6*pi*eta*r*v","variables":["F_d","eta","r","v"],"graficable":True},
{"eq":"F_b = rho*V*g","variables":["F_b","rho","V","g"],"graficable":False},
{"eq":"F_g = m*g","variables":["F_g","m","g"],"graficable":True},
{"eq":"p = m*v","variables":["p","m","v"],"graficable":True},
{"eq":"J = F*dt","variables":["J","F","dt"],"graficable":True},
{"eq":"F = m*a","variables":["F","m","a"],"graficable":True},
{"eq":"a = dv/dt","variables":["a","v","t"],"graficable":True},
{"eq":"a = v**2/r","variables":["a","v","r"],"graficable":True},
{"eq":"T = 2*pi*r/v","variables":["T","r","v"],"graficable":True},
{"eq":"omega = 2*pi/T","variables":["omega","T"],"graficable":True},
{"eq":"v = omega*r","variables":["v","omega","r"],"graficable":True}

],

# --------------------------------

"A3_energy": [

{"eq":"W = F*s*cos(theta)","variables":["W","F","s","theta"],"graficable":False},
{"eq":"E_k = 0.5*m*v**2","variables":["E_k","m","v"],"graficable":True},
{"eq":"E_p = m*g*h","variables":["E_p","m","g","h"],"graficable":True},
{"eq":"E_elastic = 0.5*k*x**2","variables":["E_elastic","k","x"],"graficable":True},
{"eq":"P = W/t","variables":["P","W","t"],"graficable":True},
{"eq":"P = F*v","variables":["P","F","v"],"graficable":True},
{"eq":"eta = useful_output/total_input","variables":["eta"],"graficable":False}

],

# --------------------------------
# B. Thermal physics
# --------------------------------

"B1_thermal": [

{"eq":"rho = m/V","variables":["rho","m","V"],"graficable":True},
{"eq":"E_k = 1.5*k_B*T","variables":["E_k","T"],"graficable":True},
{"eq":"Q = m*c*dT","variables":["Q","m","c","T"],"graficable":True},
{"eq":"Q = m*L","variables":["Q","m","L"],"graficable":True},
{"eq":"dQ_dt = k*A*dT/dx","variables":["Q","t","k","A","T","x"],"graficable":False},
{"eq":"P = sigma*A*T**4","variables":["P","A","T"],"graficable":True},
{"eq":"lambda_max*T = 2.9e-3","variables":["lambda_max","T"],"graficable":True}

],

# --------------------------------
# Gas laws
# --------------------------------

"B3_gas_laws": [

{"eq":"P = F/A","variables":["P","F","A"],"graficable":True},
{"eq":"N = n*N_A","variables":["N","n"],"graficable":True},
{"eq":"P*V/T = constant","variables":["P","V","T"],"graficable":False},
{"eq":"P*V = n*R*T","variables":["P","V","n","T"],"graficable":True},
{"eq":"P*V = N*k_B*T","variables":["P","V","N","T"],"graficable":True},
{"eq":"P = (1/3)*rho*v**2","variables":["P","rho","v"],"graficable":True},
{"eq":"U = 1.5*n*R*T","variables":["U","n","T"],"graficable":True}

],

# --------------------------------
# Waves
# --------------------------------

"C1_shm": [

{"eq":"a = -omega**2*x","variables":["a","omega","x"],"graficable":True},
{"eq":"T = 1/f","variables":["T","f"],"graficable":True},
{"eq":"omega = 2*pi*f","variables":["omega","f"],"graficable":True},
{"eq":"T = 2*pi*sqrt(m/k)","variables":["T","m","k"],"graficable":True},
{"eq":"T = 2*pi*sqrt(l/g)","variables":["T","l","g"],"graficable":True}

],

"C2_waves": [

{"eq":"v = f*lambda","variables":["v","f","lambda"],"graficable":True},
{"eq":"v = lambda/T","variables":["v","lambda","T"],"graficable":True}

],

# --------------------------------
# Fields
# --------------------------------

"D1_gravity": [

{"eq":"F = G*m1*m2/r**2","variables":["F","m1","m2","r"],"graficable":True},
{"eq":"g = G*M/r**2","variables":["g","M","r"],"graficable":True}

],

"D2_EM_fields": [

{"eq":"F = k*q1*q2/r**2","variables":["F","q1","q2","r"],"graficable":True},
{"eq":"E = F/q","variables":["E","F","q"],"graficable":True},
{"eq":"E = V/d","variables":["E","V","d"],"graficable":True}

],

"D3_motion_EM": [

{"eq":"F = q*v*B*sin(theta)","variables":["F","q","v","B","theta"],"graficable":False},
{"eq":"F = B*I*L*sin(theta)","variables":["F","B","I","L","theta"],"graficable":False}

],

# --------------------------------
# Modern physics
# --------------------------------

"E1_atom": [

{"eq":"E = h*f","variables":["E","h","f"],"graficable":True}

],

"E3_decay": [

{"eq":"E = m*c**2","variables":["E","m"],"graficable":True},
{"eq":"N = N0*exp(-lambda*t)","variables":["N","N0","lambda","t"],"graficable":True},
{"eq":"A = lambda*N","variables":["A","lambda","N"],"graficable":True},
{"eq":"T_half = log(2)/lambda","variables":["T_half","lambda"],"graficable":True}

]

}
