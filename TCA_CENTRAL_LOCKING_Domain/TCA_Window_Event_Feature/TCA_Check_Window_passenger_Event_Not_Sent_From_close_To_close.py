import sleep
TCA_Check_Window_passenger_Event_Not_Sent_From_close_To_close
Ticket_id: T2-4

Prepare:
self.press_SST()
self.check_SST_pressed()
self.set_Window_state_close(passenger_window,0)
self.check_Window_state_close(passenger_window,0)

Execute:
self.set_Window_state_close(passenger_window,0)
self.check_Window_state_close(passenger_window,0)
self.check_Window_event()


Cleanup:
self.stop_simulation("MqttController")
self.clear_all_msg_senders()
