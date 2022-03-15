import sleep
TCA_Check_Central_Locking_Event_Sent_From_UnlockedAll_To_LockedAll
Ticket_id: T2-2

Prepare:
self.press_SST()
self.check_SST_pressed()
self.set_central_locking_state_UnlockedAll(STS_y, 0x007A, ST_CLSY,1)
self.check_central_locking_state_UnlockedAll(STS_y, 0x007A, ST_CLSY,1)


Execute:
self.set_cental_locking_state_lockedAll(STS_y, 0x007A, ST_CLSY,2)
self.check_cental_locking_state_lockedAll(STS_y, 0x007A, ST_CLSY,2)
self.check_Central_Locking_event("State: lockedAll")


Cleanup:
self.stop_simulation("MqttController")
self.clear_all_msg_senders()
