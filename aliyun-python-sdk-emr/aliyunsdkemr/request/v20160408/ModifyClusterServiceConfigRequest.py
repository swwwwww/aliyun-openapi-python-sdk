# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ModifyClusterServiceConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ModifyClusterServiceConfig')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_CustomConfigParams(self):
		return self.get_query_params().get('CustomConfigParams')

	def set_CustomConfigParams(self,CustomConfigParams):
		self.add_query_param('CustomConfigParams',CustomConfigParams)

	def get_ConfigType(self):
		return self.get_query_params().get('ConfigType')

	def set_ConfigType(self,ConfigType):
		self.add_query_param('ConfigType',ConfigType)

	def get_HostInstanceId(self):
		return self.get_query_params().get('HostInstanceId')

	def set_HostInstanceId(self,HostInstanceId):
		self.add_query_param('HostInstanceId',HostInstanceId)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_ServiceName(self):
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_query_param('ServiceName',ServiceName)

	def get_Comment(self):
		return self.get_query_params().get('Comment')

	def set_Comment(self,Comment):
		self.add_query_param('Comment',Comment)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ConfigParams(self):
		return self.get_query_params().get('ConfigParams')

	def set_ConfigParams(self,ConfigParams):
		self.add_query_param('ConfigParams',ConfigParams)