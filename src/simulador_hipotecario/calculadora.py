def calcular_dividendo(monto_en_pesos, tasa_anual, plazo_anios):
    tasa_mensual = tasa_anual / 12 / 100
    numero_pagos = plazo_anios * 12
    if tasa_mensual == 0:
        dividendo = monto_en_pesos / numero_pagos
    else:
        dividendo = monto_en_pesos * (tasa_mensual * (1 + tasa_mensual) ** numero_pagos) / ((1 + tasa_mensual) ** numero_pagos - 1)

    costo_total = dividendo * numero_pagos
    return round(dividendo), round(costo_total)
