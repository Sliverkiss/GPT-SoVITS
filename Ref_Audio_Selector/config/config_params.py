import Ref_Audio_Selector.config.config_manager as config_manager

config = config_manager.get_config()

# [Base]
# 参考音频目录
reference_audio_dir = config.get_base('reference_audio_dir')

# [AudioSample]
# list转换待选参考音频目录
list_to_convert_reference_audio_dir = config.get_audio_sample('list_to_convert_reference_audio_dir')
# 音频相似度目录
audio_similarity_dir = config.get_audio_sample('audio_similarity_dir')

# [Inference]
# 默认测试文本位置
default_test_text_path = config.get_inference('default_test_text_path')
# 推理音频目录
inference_audio_dir = config.get_inference('inference_audio_dir')
# 推理音频文本聚合目录
inference_audio_text_aggregation_dir = config.get_inference('inference_audio_text_aggregation_dir')
# 推理音频情绪聚合目录
inference_audio_emotion_aggregation_dir = config.get_inference('inference_audio_emotion_aggregation_dir')

# [ResultCheck]
# asr输出文件
asr_filename = config.get_result_check('asr_filename')
# 文本相似度输出目录
text_similarity_output_dir = config.get_result_check('text_similarity_output_dir')
# 文本情绪平均相似度报告文件名
text_emotion_average_similarity_report_filename = config.get_result_check('text_emotion_average_similarity_report_filename')
# 文本相似度按情绪聚合明细文件名
text_similarity_by_emotion_detail_filename = config.get_result_check('text_similarity_by_emotion_detail_filename')
# 文本相似度按文本聚合明细文件名
text_similarity_by_text_detail_filename = config.get_result_check('text_similarity_by_text_detail_filename')

# [AudioConfig]
# 默认模板文件位置
default_template_path = config.get_audio_config('default_template_path')
# 参考音频配置文件名
reference_audio_config_filename = config.get_audio_config('reference_audio_config_filename')
