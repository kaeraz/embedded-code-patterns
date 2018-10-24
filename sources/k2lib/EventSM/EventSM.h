#ifndef SRC_EVENTSM_EVENTSM_H_
#define SRC_EVENTSM_EVENTSM_H_

typedef void (*StateFunc_T)(void);

class EventSM
{
public:
  StateFunc_T pfOnEnter;
  StateFunc_T pfOnExit;
  EventSM *pNext;
};

void EventSM_RegisterStateMachine(EventSM &pkEventSM,
                                  StateFunc_T pfStateOnEnter);
void EventSM_ChangeState(EventSM &pkEventSM, StateFunc_T pfStateOnEnter);
void EventSM_Perform();

#endif /* SRC_EVENTSM_EVENTSM_H_ */
