start = "543210"
end = "1234"
multiple = 123457
ccloop = 43999935000

while True:
    ccloop += 1
    
    cc_nr = str(ccloop * multiple)
    if cc_nr.startswith(start) and cc_nr.endswith(end):
        print(f"Credit Card Number is: {cc_nr}")