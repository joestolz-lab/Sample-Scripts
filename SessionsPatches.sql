-- run as SYS
SELECT SID,SERIAL#,USERNAME,RESOURCE_CONSUMER_GROUP FROM V$SESSION
where username = 'PBCS_REG';

select count(*) from  V$SESSION
where username = 'PBCS_REG';

-- Check patches
 select * from AIF_PATCHES ;
 -- check user POD passwords
 select * from  AIF_TARGET_APPL_PROPERTIES a
 where a.property_type IN ('CLOUD_PWD' , 'CLOUD_USER') 
 ORDER BY a.application_id;
 
 select * from  AIF_TARGET_APPL_PROPERTIES;
 -- new IF expression list
 select impgroupkey,impfldfieldname,impfldfixedtext,impfldsourcecolname,impfldtargetexp from tbhvimpitemfile ;
 -- analyze for block usage
 analyze table tdataseg
 compute statistics;
 compute sum of blocks on report
 break on report
 select extent_id, bytes, blocks
from user_extents where segment_name = 'TDATASEG' and segment_type = 'TABLE' ;
-- 8
select blocks, empty_blocks, avg_space, num_freelist_blocks from user_tables
 where table_name = 'TDATASEG'
