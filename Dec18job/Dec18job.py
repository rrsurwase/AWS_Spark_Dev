import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
# job.commit()



df= spark.read.format('csv').option("header",True).option("path","s3://dec17-glue/info.csv").load()

df.write.format('csv').option("header",True).option("path","s3://dec17-glue/dec18_op").save()        