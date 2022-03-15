import sleep
TCA_Check_Window_Driver_Event_Not_Sent_From_Open_To_Open
Ticket_id: T2-4

Prepare:
self.press_SST()
self.check_SST_pressed()
self.set_Window_state_Open(driver_window,1)
self.check_Window_state_Open(driver_window,1)

Execute:
self.set_Window_state_Open(driver_window,1)
self.check_Window_state_Open(driver_window,1)
self.check_Window_event()


Cleanup:
self.stop_simulation("MqttController")
self.clear_all_msg_senders()
