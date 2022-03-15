import sleep
TCA_Check_Central_Locking_Event_Sent_From_Locked_Patially_To_secured
Ticket_id: T2-2

Prepare:
self.press_SST()
self.check_SST_pressed()
self.set_central_locking_sate_Locked_Partially(STS_Y, 0x007A,ST_CLSY,3)
self.check_central_locking_sate_Locked_Partially(STS_Y, 0x007A,ST_CLSY,3)

Execute:
self.set_central_locking_sate_Secured(STS_Y, 0x007A,ST_CLSY,4)
self.check_central_locking_sate_secured(STS_Y, 0x007A,ST_CLSY,4)
self.check_Central_Locking_event("State: secured")

Cleanup:
self.stop_Simulation("MqttController")
self.clear_all_msg_senders()