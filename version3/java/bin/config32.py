import os
import subprocess
import sys

deltext=""
slashtext=""
copytext=""
makedir=""
org1text="org"
org2text="apache"
org3text="milagro"

if (sys.platform.startswith("linux") or sys.platform.startswith("darwin"))  :
	copytext="cp "
	deltext="rm "
	slashtext="/"
	makedir="mkdir -p "
if sys.platform.startswith("win") :
	copytext="copy "
	deltext="del "
	slashtext="\\"
	makedir="md "

def run_in_shell(cmd):
    subprocess.check_call(cmd, shell=True)

amclpath = "amcl" + slashtext + "src" + slashtext + "main" + slashtext + "java" + slashtext + org1text + slashtext + org2text + slashtext + org3text +slashtext + "amcl"
amclTestPath = "amcl" + slashtext + "src" + slashtext + "test" + slashtext + "java" + slashtext + org1text + slashtext + org2text + slashtext + org3text +slashtext + "amcl"
chosen=[]
cptr=0

def replace(namefile,oldtext,newtext):
	f = open(namefile,'r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace(oldtext,newtext)

	f = open(namefile,'w')
	f.write(newdata)
	f.close()


def rsaset(tb,nb,base,ml) :
	global deltext,slashtext,copytext
	global cptr,chosen

	chosen.append(tb)
	cptr=cptr+1

	fpath=amclpath+slashtext+tb+slashtext
	fpathTest=amclTestPath+slashtext+tb+slashtext  #ms
	run_in_shell(makedir+amclpath+slashtext+tb)
	run_in_shell(makedir+amclTestPath+slashtext+tb)  #ms

	run_in_shell(copytext+"CONFIG_BIG.java "+fpath+"CONFIG_BIG.java")
	run_in_shell(copytext+"CONFIG_FF.java "+fpath+"CONFIG_FF.java")
	run_in_shell(copytext+"BIG32.java "+fpath+"BIG.java")
	run_in_shell(copytext+"DBIG32.java "+fpath+"DBIG.java")
	run_in_shell(copytext+"FF32.java "+fpath+"FF.java")
	run_in_shell(copytext+"RSA.java "+fpath+"RSA.java")
	run_in_shell(copytext+"private_key.java "+fpath+"private_key.java")
	run_in_shell(copytext+"public_key.java "+fpath+"public_key.java")
	run_in_shell(copytext+"TestRSA.java "+fpathTest+"TestRSA.java")	#ms
	run_in_shell(copytext+"TesttimeRSA.java "+fpathTest+"TesttimeRSA.java")	#ms

	replace(fpath+"CONFIG_BIG.java","XXX",tb)
	replace(fpath+"CONFIG_FF.java","XXX",tb)
	replace(fpath+"BIG.java","XXX",tb)
	replace(fpath+"DBIG.java","XXX",tb)
	replace(fpath+"FF.java","XXX",tb)
	replace(fpath+"RSA.java","XXX",tb)
	replace(fpath+"private_key.java","XXX",tb)
	replace(fpath+"public_key.java","XXX",tb)
	replace(fpathTest+"TestRSA.java","XXX",tb)  #ms
	replace(fpathTest+"TesttimeRSA.java","XXX",tb)  #ms

	replace(fpath+"CONFIG_BIG.java","@NB@",nb)
	replace(fpath+"CONFIG_BIG.java","@BASE@",base)

	replace(fpath+"CONFIG_FF.java","@ML@",ml)


def curveset(tc,nb,base,nbt,m8,mt,ct,pf,stw,sx,ab,cs) :
	global deltext,slashtext,copytext
	global cptr,chosen

	chosen.append(tc)
	cptr=cptr+1

	fpath=amclpath+slashtext+tc+slashtext
	fpathTest=amclTestPath+slashtext+tc+slashtext  #ms
	run_in_shell(makedir+amclpath+slashtext+tc)
	run_in_shell(makedir+amclTestPath+slashtext+tc)  #ms

	run_in_shell(copytext+"CONFIG_BIG.java "+fpath+"CONFIG_BIG.java")
	run_in_shell(copytext+"CONFIG_FIELD.java "+fpath+"CONFIG_FIELD.java")
	run_in_shell(copytext+"CONFIG_CURVE.java "+fpath+"CONFIG_CURVE.java")
	run_in_shell(copytext+"BIG32.java "+fpath+"BIG.java")
	run_in_shell(copytext+"DBIG32.java "+fpath+"DBIG.java")
	run_in_shell(copytext+"FP32.java "+fpath+"FP.java")
	run_in_shell(copytext+"ECP.java "+fpath+"ECP.java")
	run_in_shell(copytext+"ECDH.java "+fpath+"ECDH.java")
	run_in_shell(copytext+"ROM_"+tc+"_32.java "+fpath+"ROM.java")
	run_in_shell(copytext+"TestECDH.java "+fpathTest+"TestECDH.java")	#ms
	run_in_shell(copytext+"TesttimeECDH.java "+fpathTest+"TesttimeECDH.java")	#ms

	replace(fpath+"CONFIG_BIG.java","XXX",tc)
	replace(fpath+"CONFIG_FIELD.java","XXX",tc)
	replace(fpath+"CONFIG_CURVE.java","XXX",tc)
	replace(fpath+"BIG.java","XXX",tc)
	replace(fpath+"DBIG.java","XXX",tc)
	replace(fpath+"FP.java","XXX",tc)
	replace(fpath+"ECP.java","XXX",tc)
	replace(fpath+"ECDH.java","XXX",tc)
	replace(fpathTest+"TestECDH.java","XXX",tc)  #ms
	replace(fpathTest+"TesttimeECDH.java","XXX",tc)  #ms

	replace(fpath+"CONFIG_BIG.java","@NB@",nb)
	replace(fpath+"CONFIG_BIG.java","@BASE@",base)

	replace(fpath+"CONFIG_FIELD.java","@NBT@",nbt)
	replace(fpath+"CONFIG_FIELD.java","@M8@",m8)
	replace(fpath+"CONFIG_FIELD.java","@MT@",mt)

	ib=int(base)
	inb=int(nb)
	inbt=int(nbt)
	sh=ib*(1+((8*inb-1)//ib))-inbt
	if sh > 14 :
		sh=14
	replace(fpath+"CONFIG_FIELD.java","@SH@",str(sh))


	replace(fpath+"CONFIG_CURVE.java","@CT@",ct)
	replace(fpath+"CONFIG_CURVE.java","@PF@",pf)

	replace(fpath+"CONFIG_CURVE.java","@ST@",stw)
	replace(fpath+"CONFIG_CURVE.java","@SX@",sx)
	replace(fpath+"CONFIG_CURVE.java","@AB@",ab)

	if cs == "128" :
		replace(fpath+"CONFIG_CURVE.java","@HT@","32")
		replace(fpath+"CONFIG_CURVE.java","@AK@","16")
	if cs == "192" :
		replace(fpath+"CONFIG_CURVE.java","@HT@","48")
		replace(fpath+"CONFIG_CURVE.java","@AK@","24")
	if cs == "256" :
		replace(fpath+"CONFIG_CURVE.java","@HT@","64")
		replace(fpath+"CONFIG_CURVE.java","@AK@","32")

	if pf != "NOT" :
		run_in_shell(copytext+"FP2.java "+fpath+"FP2.java")
		run_in_shell(copytext+"FP4.java "+fpath+"FP4.java")

		replace(fpath+"FP2.java","XXX",tc)
		replace(fpath+"FP4.java","XXX",tc)

		if cs == "128" :

			run_in_shell(copytext+"ECP2.java "+fpath+"ECP2.java")
			run_in_shell(copytext+"FP12.java "+fpath+"FP12.java")
			run_in_shell(copytext+"PAIR.java "+fpath+"PAIR.java")
			run_in_shell(copytext+"MPIN.java "+fpath+"MPIN.java")
			run_in_shell(copytext+"BLS.java "+fpath+"BLS.java")
			run_in_shell(copytext+"TestMPIN.java "+fpathTest+"TestMPIN.java")	#ms
			run_in_shell(copytext+"TestBLS.java "+fpathTest+"TestBLS.java")	#ms
			run_in_shell(copytext+"TesttimeMPIN.java "+fpathTest+"TesttimeMPIN.java")	#ms

			replace(fpath+"FP12.java","XXX",tc)
			replace(fpath+"ECP2.java","XXX",tc)
			replace(fpath+"PAIR.java","XXX",tc)
			replace(fpath+"MPIN.java","XXX",tc)
			replace(fpath+"BLS.java","XXX",tc)
			replace(fpathTest+"TestMPIN.java","XXX",tc)  #ms
			replace(fpathTest+"TestBLS.java","XXX",tc)  #ms
			replace(fpathTest+"TesttimeMPIN.java","XXX",tc)  #ms

		if cs == "192" :
			run_in_shell(copytext+"ECP4.java "+fpath+"ECP4.java")
			run_in_shell(copytext+"FP8.java "+fpath+"FP8.java")
			run_in_shell(copytext+"FP24.java "+fpath+"FP24.java")
			run_in_shell(copytext+"PAIR192.java "+fpath+"PAIR192.java")
			run_in_shell(copytext+"MPIN192.java "+fpath+"MPIN192.java")
			run_in_shell(copytext+"BLS192.java "+fpath+"BLS192.java")
			run_in_shell(copytext+"TestMPIN192.java "+fpathTest+"TestMPIN192.java")	#ms
			run_in_shell(copytext+"TestBLS192.java "+fpathTest+"TestBLS192.java")	#ms
			run_in_shell(copytext+"TesttimeMPIN192.java "+fpathTest+"TesttimeMPIN192.java")	#ms

			replace(fpath+"FP8.java","XXX",tc)
			replace(fpath+"FP24.java","XXX",tc)
			replace(fpath+"ECP4.java","XXX",tc)
			replace(fpath+"PAIR192.java","XXX",tc)
			replace(fpath+"MPIN192.java","XXX",tc)
			replace(fpath+"BLS192.java","XXX",tc)
			replace(fpathTest+"TestMPIN192.java","XXX",tc)  #ms
			replace(fpathTest+"TestBLS192.java","XXX",tc)  #ms
			replace(fpathTest+"TesttimeMPIN192.java","XXX",tc)  #ms

		if cs == "256" :
			run_in_shell(copytext+"FP8.java "+fpath+"FP8.java")
			run_in_shell(copytext+"ECP8.java "+fpath+"ECP8.java")
			run_in_shell(copytext+"FP16.java "+fpath+"FP16.java")
			run_in_shell(copytext+"FP48.java "+fpath+"FP48.java")
			run_in_shell(copytext+"PAIR256.java "+fpath+"PAIR256.java")
			run_in_shell(copytext+"MPIN256.java "+fpath+"MPIN256.java")
			run_in_shell(copytext+"BLS256.java "+fpath+"BLS256.java")
			run_in_shell(copytext+"TestMPIN256.java "+fpathTest+"TestMPIN256.java")	#ms
			run_in_shell(copytext+"TestBLS256.java "+fpathTest+"TestBLS256.java")	#ms
			run_in_shell(copytext+"TesttimeMPIN256.java "+fpathTest+"TesttimeMPIN256.java")	#ms

			replace(fpath+"FP8.java","XXX",tc)
			replace(fpath+"FP16.java","XXX",tc)
			replace(fpath+"FP48.java","XXX",tc)
			replace(fpath+"ECP8.java","XXX",tc)
			replace(fpath+"PAIR256.java","XXX",tc)
			replace(fpath+"MPIN256.java","XXX",tc)
			replace(fpath+"BLS256.java","XXX",tc)
			replace(fpathTest+"TestMPIN256.java","XXX",tc)  #ms
			replace(fpathTest+"TestBLS256.java","XXX",tc)  #ms
			replace(fpathTest+"TesttimeMPIN256.java","XXX",tc)  #ms


run_in_shell(makedir + amclpath)

run_in_shell(copytext + "pom.xml " + "amcl" + slashtext + ".")
for file in ['HASH*.java', 'SHA3.java', 'RAND.java', 'AES.java', 'GCM.java', 'NHS.java']:
	run_in_shell(copytext + file + " " + amclpath+slashtext+".")

print("Elliptic Curves")
print("1. ED25519")
print("2. C25519")
print("3. NIST256")
print("4. BRAINPOOL")
print("5. ANSSI")
print("6. HIFIVE")
print("7. GOLDILOCKS")
print("8. NIST384")
print("9. C41417")
print("10. NIST521\n")
print("11. NUMS256W")
print("12. NUMS256E")
print("13. NUMS384W")
print("14. NUMS384E")
print("15. NUMS512W")
print("16. NUMS512E")
print("17. SECP256K1\n")


print("Pairing-Friendly Elliptic Curves")
print("18. BN254")
print("19. BN254CX")
print("20. BLS383")
print("21. BLS381")
print("22. FP256BN")
print("23. FP512BN")
print("24. BLS461\n")

print("25. BLS24")
print("26. BLS48\n")

print("RSA")
print("27. RSA2048")
print("28. RSA3072")
print("29. RSA4096")

selection=[]
ptr=0
max=30

curve_selected=False
pfcurve_selected=False
rsa_selected=False

while ptr<max:
	x=int(input("Choose a Scheme to support - 0 to finish: "))
	if x == 0:
		break
#	print("Choice= ",x)
	already=False
	for i in range(0,ptr):
		if x==selection[i]:
			already=True
			break
	if already:
		continue

	selection.append(x)
	ptr=ptr+1

# curveset(curve,big_length_bytes,bits_in_base,modulus_bits,modulus_mod_8,modulus_type,curve_type,pairing_friendly,sextic twist,sign of x,curve security)
# where "curve" is the common name for the elliptic curve
# big_length_bytes is the modulus size rounded up to a number of bytes
# bits_in_base gives the number base used for 32 bit architectures, as n where the base is 2^n
# modulus_bits is the actual bit length of the modulus.
# modulus_mod_8 is the remainder when the modulus is divided by 8
# modulus_type is NOT_SPECIAL, or PSEUDO_MERSENNE, or MONTGOMERY_Friendly, or GENERALISED_MERSENNE (supported for GOLDILOCKS only)
# curve_type is WEIERSTRASS, EDWARDS or MONTGOMERY
# pairing_friendly is BN, BLS or NOT (if not pairing friendly)
# if pairing friendly. M or D type twist, and sign of the family parameter x
# curve security is AES equiavlent, rounded up.


	if x==1:
		curveset("ED25519","32","29","255","5","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","NOT","128")
		curve_selected=True
	if x==2:
		curveset("C25519","32","29","255","5","PSEUDO_MERSENNE","MONTGOMERY","NOT","NOT","NOT","NOT","128")
		curve_selected=True
	if x==3:
		curveset("NIST256","32","28","256","7","NOT_SPECIAL","WEIERSTRASS","NOT","NOT","NOT","NOT","128")   # Change to 28
		curve_selected=True
	if x==4:
		curveset("BRAINPOOL","32","28","256","7","NOT_SPECIAL","WEIERSTRASS","NOT","NOT","NOT","NOT","128") # Change to 28
		curve_selected=True
	if x==5:
		curveset("ANSSI","32","28","256","7","NOT_SPECIAL","WEIERSTRASS","NOT","NOT","NOT","NOT","128") # Change to 28
		curve_selected=True

	if x==6:
		curveset("HIFIVE","42","29","336","5","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","NOT","192")
		curve_selected=True
	if x==7:
		curveset("GOLDILOCKS","56","29","448","7","GENERALISED_MERSENNE","EDWARDS","NOT","NOT","NOT","NOT","256")
		curve_selected=True
	if x==8:
		curveset("NIST384","48","29","384","7","NOT_SPECIAL","WEIERSTRASS","NOT","NOT","NOT","NOT","192")  # change to 29
		curve_selected=True
	if x==9:
		curveset("C41417","52","29","414","7","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","NOT","256")
		curve_selected=True
	if x==10:
		curveset("NIST521","66","28","521","7","PSEUDO_MERSENNE","WEIERSTRASS","NOT","NOT","NOT","NOT","256")
		curve_selected=True

	if x==11:
		curveset("NUMS256W","32","28","256","3","PSEUDO_MERSENNE","WEIERSTRASS","NOT","NOT","NOT","NOT","128")
		curve_selected=True
	if x==12:
		curveset("NUMS256E","32","29","256","3","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","NOT","128")
		curve_selected=True
	if x==13:
		curveset("NUMS384W","48","29","384","3","PSEUDO_MERSENNE","WEIERSTRASS","NOT","NOT","NOT","NOT","192")
		curve_selected=True
	if x==14:
		curveset("NUMS384E","48","29","384","3","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","NOT","192")
		curve_selected=True
	if x==15:
		curveset("NUMS512W","64","29","512","7","PSEUDO_MERSENNE","WEIERSTRASS","NOT","NOT","NOT","NOT","256")
		curve_selected=True
	if x==16:
		curveset("NUMS512E","64","29","512","7","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","NOT","256")
		curve_selected=True
	if x==17:
		curveset("SECP256K1","32","28","256","7","NOT_SPECIAL","WEIERSTRASS","NOT","NOT","NOT","NOT","128")   # Change to 28
		curve_selected=True

	if x==18:
		curveset("BN254","32","28","254","3","NOT_SPECIAL","WEIERSTRASS","BN","D_TYPE","NEGATIVEX","66","128")
		pfcurve_selected=True
	if x==19:
		curveset("BN254CX","32","28","254","3","NOT_SPECIAL","WEIERSTRASS","BN","D_TYPE","NEGATIVEX","66","128")
		pfcurve_selected=True
	if x==20:
		curveset("BLS383","48","29","383","3","NOT_SPECIAL","WEIERSTRASS","BLS","M_TYPE","POSITIVEX","65","128")
		pfcurve_selected=True

	if x==21:
		curveset("BLS381","48","29","381","3","NOT_SPECIAL","WEIERSTRASS","BLS","M_TYPE","NEGATIVEX","65","128")
		pfcurve_selected=True


	if x==22:
		curveset("FP256BN","32","28","256","3","NOT_SPECIAL","WEIERSTRASS","BN","M_TYPE","NEGATIVEX","66","128")
		pfcurve_selected=True
	if x==23:
		curveset("FP512BN","64","29","512","3","NOT_SPECIAL","WEIERSTRASS","BN","M_TYPE","POSITIVEX","130","128")
		pfcurve_selected=True
# https://eprint.iacr.org/2017/334.pdf
	if x==24:
		curveset("BLS461","58","28","461","3","NOT_SPECIAL","WEIERSTRASS","BLS","M_TYPE","NEGATIVEX","78","128")
		pfcurve_selected=True


	if x==25:
		curveset("BLS24","60","29","479","3","NOT_SPECIAL","WEIERSTRASS","BLS","M_TYPE","POSITIVEX","49","192")
		pfcurve_selected=True
	if x==26:
		curveset("BLS48","70","29","556","3","NOT_SPECIAL","WEIERSTRASS","BLS","M_TYPE","POSITIVEX","32","256")
		pfcurve_selected=True



# rsaset(rsaname,big_length_bytes,bits_in_base,multiplier)
# The RSA name reflects the modulus size, which is a 2^m multiplier
# of the underlying big length

# There are choices here, different ways of getting the same result, but some faster than others
	if x==27:
		#256 is slower but may allow reuse of 256-bit BIGs used for elliptic curve
		#512 is faster.. but best is 1024
		rsaset("RSA2048","128","28","2")
		#rsaset("RSA2048","64","29","4")
		#rsaset("RSA2048","32","29","8")
		rsa_selected=True
	if x==28:
		rsaset("RSA3072","48","28","8")
		rsa_selected=True
	if x==29:
		#rsaset("RSA4096","32","29","16")
		rsaset("RSA4096","64","29","8")
		rsa_selected=True

