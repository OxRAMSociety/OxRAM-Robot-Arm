#!/usr/bin/env python3

import rospy
import smach
import smach_ros
import random


class stateA(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['SUCCESS','FAILURE'], output_keys=['A_count'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo("Executing State A...")
        r.sleep()

        self.counter += 1
        userdata.A_count = self.counter
        
        result = random.choice(['SUCCESS','FAILURE'])	# Determine next state

        return result


class stateB(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['SUCCESS','FAILURE'], output_keys=['B_count'])
        self.counter = 0

    def execute(self, userdata):

        rospy.loginfo("Executing State B...")
        r.sleep()

        self.counter +=1
        userdata.B_count = self.counter

        result = random.choice(['SUCCESS','FAILURE'])	# Determine next state

        return result


class stateC(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['SUCCESS','FAILURE'], output_keys=['C_count'])
        self.counter = 0

    def execute(self, userdata):

        rospy.loginfo("Executing State C...")
        r.sleep()

        self.counter += 1
        userdata.C_count = self.counter
        
        result = random.choice(['SUCCESS','FAILURE'])	# Determine next state

        return result


if __name__ == '__main__':
    rospy.init_node('ExampleStateMachineNode')

    r = rospy.Rate(2)

    sm = smach.StateMachine(outcomes=['end'])

    with sm:
        smach.StateMachine.add('A', stateA(), transitions={'FAILURE':'A','SUCCESS':'B'})

        smach.StateMachine.add('B', stateB(), transitions={'FAILURE':'A','SUCCESS':'C'})

        smach.StateMachine.add('C', stateC(), transitions={'FAILURE':'A','SUCCESS':'end'})

    # To exit the State Machine, Tasks A, B, and C must each be successfully completed in order
    # Each Task has a 50 percent chance of success
    # If any Task fails, re-start from Task A

    sm.userdata.A_count = 0
    sm.userdata.B_count = 0
    sm.userdata.C_count = 0

    outcome = sm.execute()

    rospy.loginfo("State A Attempted %d Times", sm.userdata.A_count)
    rospy.loginfo("State B Attempted %d Times", sm.userdata.B_count)
    rospy.loginfo("State C Attempted %d Times", sm.userdata.C_count)
