APIKEY='183f54cec6a53ca064d93fbf6399a465'
name='虚拟机备份作业1'

curl 'http://192.168.3.117/ds/dbackup/' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H "X-API-Key: $APIKEY" \
  --data-urlencode "module_type=2" \
  --data-urlencode "func=CreateBackupTask" \
  --data-urlencode 'params={"fusion_cloud_param":{},"fusion_backup_server_info":{},"vcenter_id":"1","backup_vm_group_id":"","backup_target_type":"1","backup_host_uuid":"","backup_target_clue":"","module_type":"1","backup_type":"1","task_type":"1","task_name":"'$name'","host_uuids":["f1333bdc-fabb-4c4f-8e76-09cbee1139a3"],"vm_uuids":[{"vm_uuid":"421212d1-0798-920e-e382-17e40d17da3d","dest_host_id":"1"}],"vm_names":[],"resource":"","client_names":[],"vmDisplayType":"2","vmBackType":"1","oncetime":"","time_strategy_info":{"strategy_type":"11","start_time":"2023-09-20 09:00:58","start_now":"0","fullInfo":{"policyType":"11"},"diffInfo":{},"increInfo":{},"syntheticInfo":{}},"transport_mode":"2","lun_path":"","lun_name":"","compress_format":"1","storage_format":"1","deduplication_flag":"0","scan_whole_disk_flag":"0","net_limit_strategy":{"finish_time":"0","is_enable":"0","net_speed":"","start_time":"0"},"netlimit_strategy_info":{"is_enable":"0","net_speed":"0"},"only_fullbackup_flag":"0","is_dedup":"0","storage_uuid":"c32d3d50579411ee8000005056920a0d","storage_name":"catalog","host_id_for_huawei":"0","backup_host_id":"0","backup_new_vm_flag":"0","start_now_flag":"0","task_mode":"3","job_type":"backup","is_source_dedup":"0","api_type":"1","fc_lun_info":{"fc_lun_number":"","fc_lun_id":"","fc_device_uuid":"","fc_lun_target_name":"","fc_bind_agent_uuid":""},"vm_filters":[],"backup_disks":"all_disks","proxy_host":"","proxy_uuid":"","valid_data":0,"reserve_snapshot":"0","disks":{},"tenant_uuid":"da398bbe579111ee8000005056920a0d","user_uuid":"ca718c049b90000164b91130326071b0","user_name":"scutech","language":"zh-CN"}'


