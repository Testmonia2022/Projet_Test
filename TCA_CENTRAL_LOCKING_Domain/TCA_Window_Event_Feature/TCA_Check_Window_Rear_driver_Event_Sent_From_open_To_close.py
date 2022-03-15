import sleep
TCA_Check_Window_Rear_driver_Event_Sent_From_open_To_close
Ticket_id: T2-4

Prepare:
self.press_SST()
self.check_SST_pressed()
self.set_Window_state_open(Rear_driver_window,1)
self.check_Window_state_open(Rear_driver_window,1)

Execute:
self.set_Window_state_close(Rear_driver_window,0)
self.check_Window_state_close(Rear_driver_window,0)
self.check_Window_event("State: close")


Cleanup:
self.stop_simulation("MqttController")
self.clear_all_msg_senders()
