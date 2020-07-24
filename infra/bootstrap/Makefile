.PHONY: deploy
deploy_jenkins:
	sh create.sh jenkins-infra aws_infra.yml params.json

deploy_k8s_cluster
	eksctl create cluster -f eksctl_config.yml
