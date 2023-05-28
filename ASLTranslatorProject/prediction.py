def translation():
    import omegaconf
    from openhands.apis.inference import InferenceModel

    cfg = omegaconf.OmegaConf.load("/home/tester/finalProject/wlasl/st_gcn/config.yaml")
    model = InferenceModel(cfg=cfg)
    model.init_from_checkpoint_if_available()
    cfg.data.test_pipeline.dataset.inference_mode = True
    if cfg.data.test_pipeline.dataset.inference_mode:
        model.test_inference()
    else:
        model.compute_test_accuracy()

if __name__ == "__main__":
    translation()
