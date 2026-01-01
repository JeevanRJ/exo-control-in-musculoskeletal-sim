import os


def Assist(
    context,
    istep,
    filenameistep,
    filenamefsrfront,
    filenamefsrrear,
):
   
    filelocationistep = os.path.join(filenameistep)   
    filelocationfsrfront = os.path.join(filenamefsrfront) 
    filelocationfsrrear = os.path.join(filenamefsrrear)
    
    # read simulation step value
    try:
        with open(filelocationistep, "r") as f0:
            prev_istep = float(f0.read())
    except IOError:
        prev_istep = 0


    # read value of FSR_front
    try:
        with open(filelocationfsrfront, "r") as f:
            FSR_Front = float(f.read())
    except IOError:
        FSR_Front = 0

    # read value of FSR_rear
    try:
        with open(filelocationfsrrear, "r") as f2:
            FSR_Rear = float(f2.read())
    except IOError:
        FSR_Rear = 0



    # set previous assistance to 0.0 if first time-step
    if istep == 0:
        FSR_Front = 0
    if istep == 0:
        FSR_Rear = 0

    # if the function is called multiple times at the same time-step, return

    with open(filelocationistep, "w") as fi:
        fi.write(f"{istep}")


    if FSR_Front > -30 :
       F = 1;
    else: 
       F = 0
        
    # return assistive torque
    return F