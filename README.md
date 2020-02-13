# MOCIModesScheduling

This is used for scheduling modes for MOCI using STK given a target list
and using the ground station on top of the Geography Building at the 
University of Georgia. This chooses between four modes: data downlink, 
imaging, image processing, cruise.

## Running

`python main.py`

Then follow the on-screen instructions.

## Scheduling

Scheduling follows the following precedent:
1. Data downlink
2. Imaging + data processing
3. Cruise mode

This means that data downlink is always chosen if the opportunity is given.
With data downlink opportunities chosen, the access is parsed and chosen off
the following criteria: if the time of the access plus 30 minutes for a transition
to data processing mode does not conflict with any previously scheduled modes.
The remaining time between the modes is automatically scheduled as cruise mode.

## Known Limitations

As it currently stands, the scheduler makes certain assumptions about
the process:
1. We take advantage of all data downlink opportunities no matter how short.
2. Image processing mode will immediately follow imaging mode.
3. Image processing mode takes exactly 30 minutes.
4. After ruling out target access based on conflict with ground station
passes, the scheduler takes advantage of all imaging opportunities.
5. The scheduler goes into cruise mode at all available opportunities after
other modes have been scheduled.
    
These assumptions can lead to errors but give a fair and simple schedule. 
In order to take advantage of more accurate schedules, the scheduler method
will need to be adjusted.