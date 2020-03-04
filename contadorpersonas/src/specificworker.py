#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

from genericworker import *

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# sys.path.append('/opt/robocomp/lib')
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel

class SpecificWorker(GenericWorker):
	def __init__(self, proxy_map):
		super(SpecificWorker, self).__init__(proxy_map)
		self.Period = 10
		self.timer.start(self.Period)
		self.people_data = PeopleData()

		self.defaultMachine.start()
		self.destroyed.connect(self.t_compute_to_finalize)

	def __del__(self):
		print('SpecificWorker destructor')

	def setParams(self, params):
		try:
			self.innermodel = InnerModel(params["InnerModelPath"])
		except:
			traceback.print_exc()
			print("Error reading config params")
		return True

	@QtCore.Slot()
	def compute(self):

		#QVec::vec6 point = {0,0,0,0,0,0};
		#result = self.innermodel.transform6D("world", "rgbd_1", point)

		cuenta = 0
		for i in range(1, 10):
			cuenta = cuenta + len(self.people_data.peoplelist)
		
		salida = cuenta/10
		print('Hay '+salida+' Personas en la sala')
		#print(len(self.people_data.peoplelist))
		return True

# =============== Slots methods for State Machine ===================
# ===================================================================
	#
	# sm_initialize
	#
	@QtCore.Slot()
	def sm_initialize(self):
		print("Entered state initialize")
		self.t_initialize_to_compute.emit()
		pass

	#
	# sm_compute
	#
	@QtCore.Slot()
	def sm_compute(self):
		print("Entered state compute")
		self.compute()
		pass

	#
	# sm_finalize
	#
	@QtCore.Slot()
	def sm_finalize(self):
		print("Entered state finalize")
		pass


# =================================================================
# SUBSCRIPTION
# =================================================================


	#
	# newPeopleData
	#
	def HumanCameraBody_newPeopleData(self, people):
		self.people_data = people
		

