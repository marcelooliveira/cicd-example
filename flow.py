from prefect import flow

@flow(log_prints=True)
def hello():
  print("Hello!")

if __name__ == "__main__":
    hello.deploy(
        name="cicd-deployment",
        work_pool_name="my-work-pool",
        image="mclricardo/cicd_image:latest",
    )
