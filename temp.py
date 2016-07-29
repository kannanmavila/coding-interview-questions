required_fields = ["server['server_name']","server['server_info']['asset_type']['display_name']",
                   "server['asset_status']['display_name']", "server['record_owner']['group_name']",
                   "server['server_total_cost_of_ownership']['description']",
                   "server['primary_business_owner']['name']", "server['environment']['display_name']",
                   "server['is_virtual']", "server['managed_by']['display_name']",
                   "server['server_info']['billable_ibm']", "server['server_info']['billing_sub_type']['display_name']",
                   "server['server_info']['serial_number']", "", "server['location']['display_name']",
                   "server['inception_date']", "server['server_info']['decommission_date']" ]

for server in server_list:
    for item in required_fields:
        print item