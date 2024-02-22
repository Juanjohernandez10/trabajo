#un estudainte debe realizar su proceso de matricula teniendo en cuenta lo siguiente el estudiante debe 
#tomar una cantidad de creditos dividida por semestre 

cons_costo1semestre = 15 * 28000
cons_costo2semestre = 10 * 35000
cons_costo3semestre = 12 * 40000
cons_costo4semestre = 11 * 45000
cons_costo5semestre = 16 * 55000
cons_costo6semestre = 17 * 60000
cons_costo7semestre = 9 * 75000
cons_costo8semestre = 18 * 80000
cons_costo9semestre = 12 * 95000
cons_costo10semestre = 17 * 110000

var_nombre_aspiranteStr = input('Nombre ->')
var_capacidad_semestreFlt = float(input('presupuesto'))

var_matriculaInt = int(input('- - semestre- - /n/n1. semestre1 /n2. semestre2 /n3. semestre3 /n4. semestre4/n5. semestre5/n6. semestre6/n7. semestre7/n8. semestre8/n9. semestre9/n10. semestre10 n->'))

if var_matriculaInt == 1:
    var_matriculaInt = cons_costo1semestre
if var_matriculaInt == 2:
    var_matriculaInt = cons_costo2semestre
if var_matriculaInt == 3:
    var_matriculaInt = cons_costo3semestre
if var_matriculaInt == 4:
    var_matriculaInt = cons_costo4semestre
if var_matriculaInt == 5:
    var_matriculaInt = cons_costo5semestre
if var_matriculaInt == 6:
    var_matriculaInt = cons_costo6semestre
if var_matriculaInt == 7:
    var_matriculaInt = cons_costo7semestre
if var_matriculaInt == 8:
    var_matriculaInt = cons_costo8semestre
    
