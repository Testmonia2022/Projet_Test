import sleep
TCA_Check_Driver_Door_Event_Sent_From_Open_To_Close
Ticket_id: T2-3

Prepare:
self.press_SST()
self.check_SST_pressed()
self.set_Door_state_Open(driver_door,1)
self.check_Door_state_Open(driver_door,1)

Execute:
self.set_Door_state_Close(driver_door,0)
self.check_Door_state_Close(driver_door,0)
self.check_Door_event(driver_door, "State: Close")


Cleanup:
self.stop_simulation("MqttController")
self.clear_all_msg_senders()
