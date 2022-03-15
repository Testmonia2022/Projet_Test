import sleep
TCA_Check_Passenger_Door_Event_Sent_From_Close_To_Close
Ticket_id: T2-3

Prepare:
self.press_SST()
self.check_SST_pressed()
self.set_Door_state_Close(Passenger_door,0)
self.check_Door_state_Close(Passenger_door,0)

Execute:
self.set_Door_state_Close(Passenger_door,0)
self.check_Door_state_Close(Passenger_door,0)
self.check_Door_event()


Cleanup:
self.stop_simulation("MqttController")
self.clear_all_msg_senders()
