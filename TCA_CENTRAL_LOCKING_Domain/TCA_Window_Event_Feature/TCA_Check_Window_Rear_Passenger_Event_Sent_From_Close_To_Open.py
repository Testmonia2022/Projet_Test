import sleep
TCA_Check_Window_Rear_Passenger_Event_Sent_From_Close_To_Open
Ticket_id: T2-4

Prepare:
self.press_SST()
self.check_SST_pressed()
self.set_Window_state_Close(Rear_passenger_window,0)
self.check_Window_state_Close(Rear_passenger_window,0)

Execute:
self.set_Window_state_Open(Rear_passenger_window,1)
self.check_Window_state_Open(Rear_passenger_window,1)
self.check_Window_event("State: Open")


Cleanup:
self.stop_simulation("MqttController")
self.clear_all_msg_senders()
