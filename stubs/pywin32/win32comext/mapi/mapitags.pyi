from _typeshed import Incomplete

MV_FLAG: int
PT_UNSPECIFIED: int
PT_NULL: int
PT_I2: int
PT_LONG: int
PT_R4: int
PT_DOUBLE: int
PT_CURRENCY: int
PT_APPTIME: int
PT_ERROR: int
PT_BOOLEAN: int
PT_OBJECT: int
PT_I8: int
PT_STRING8: int
PT_UNICODE: int
PT_SYSTIME: int
PT_CLSID: int
PT_BINARY: int
PT_SHORT: int
PT_I4: int
PT_FLOAT: int
PT_R8: int
PT_LONGLONG: int
PT_MV_I2: Incomplete
PT_MV_LONG: Incomplete
PT_MV_R4: Incomplete
PT_MV_DOUBLE: Incomplete
PT_MV_CURRENCY: Incomplete
PT_MV_APPTIME: Incomplete
PT_MV_SYSTIME: Incomplete
PT_MV_STRING8: Incomplete
PT_MV_BINARY: Incomplete
PT_MV_UNICODE: Incomplete
PT_MV_CLSID: Incomplete
PT_MV_I8: Incomplete
PT_MV_SHORT: Incomplete
PT_MV_I4: Incomplete
PT_MV_FLOAT: Incomplete
PT_MV_R8: Incomplete
PT_MV_LONGLONG: Incomplete
PT_TSTRING: int
PT_MV_TSTRING: Incomplete
PROP_TYPE_MASK: int

def PROP_TYPE(ulPropTag): ...
def PROP_ID(ulPropTag): ...
def PROP_TAG(ulPropType, ulPropID): ...

PROP_ID_NULL: int
PROP_ID_INVALID: int
PR_NULL: Incomplete
PR_ACKNOWLEDGEMENT_MODE: Incomplete
PR_ALTERNATE_RECIPIENT_ALLOWED: Incomplete
PR_AUTHORIZING_USERS: Incomplete
PR_AUTO_FORWARD_COMMENT: Incomplete
PR_AUTO_FORWARD_COMMENT_W: Incomplete
PR_AUTO_FORWARD_COMMENT_A: Incomplete
PR_AUTO_FORWARDED: Incomplete
PR_CONTENT_CONFIDENTIALITY_ALGORITHM_ID: Incomplete
PR_CONTENT_CORRELATOR: Incomplete
PR_CONTENT_IDENTIFIER: Incomplete
PR_CONTENT_IDENTIFIER_W: Incomplete
PR_CONTENT_IDENTIFIER_A: Incomplete
PR_CONTENT_LENGTH: Incomplete
PR_CONTENT_RETURN_REQUESTED: Incomplete
PR_CONVERSATION_KEY: Incomplete
PR_CONVERSION_EITS: Incomplete
PR_CONVERSION_WITH_LOSS_PROHIBITED: Incomplete
PR_CONVERTED_EITS: Incomplete
PR_DEFERRED_DELIVERY_TIME: Incomplete
PR_DELIVER_TIME: Incomplete
PR_DISCARD_REASON: Incomplete
PR_DISCLOSURE_OF_RECIPIENTS: Incomplete
PR_DL_EXPANSION_HISTORY: Incomplete
PR_DL_EXPANSION_PROHIBITED: Incomplete
PR_EXPIRY_TIME: Incomplete
PR_IMPLICIT_CONVERSION_PROHIBITED: Incomplete
PR_IMPORTANCE: Incomplete
PR_IPM_ID: Incomplete
PR_LATEST_DELIVERY_TIME: Incomplete
PR_MESSAGE_CLASS: Incomplete
PR_MESSAGE_CLASS_W: Incomplete
PR_MESSAGE_CLASS_A: Incomplete
PR_MESSAGE_DELIVERY_ID: Incomplete
PR_MESSAGE_SECURITY_LABEL: Incomplete
PR_OBSOLETED_IPMS: Incomplete
PR_ORIGINALLY_INTENDED_RECIPIENT_NAME: Incomplete
PR_ORIGINAL_EITS: Incomplete
PR_ORIGINATOR_CERTIFICATE: Incomplete
PR_ORIGINATOR_DELIVERY_REPORT_REQUESTED: Incomplete
PR_ORIGINATOR_RETURN_ADDRESS: Incomplete
PR_PARENT_KEY: Incomplete
PR_PRIORITY: Incomplete
PR_ORIGIN_CHECK: Incomplete
PR_PROOF_OF_SUBMISSION_REQUESTED: Incomplete
PR_READ_RECEIPT_REQUESTED: Incomplete
PR_RECEIPT_TIME: Incomplete
PR_RECIPIENT_REASSIGNMENT_PROHIBITED: Incomplete
PR_REDIRECTION_HISTORY: Incomplete
PR_RELATED_IPMS: Incomplete
PR_ORIGINAL_SENSITIVITY: Incomplete
PR_LANGUAGES: Incomplete
PR_LANGUAGES_W: Incomplete
PR_LANGUAGES_A: Incomplete
PR_REPLY_TIME: Incomplete
PR_REPORT_TAG: Incomplete
PR_REPORT_TIME: Incomplete
PR_RETURNED_IPM: Incomplete
PR_SECURITY: Incomplete
PR_INCOMPLETE_COPY: Incomplete
PR_SENSITIVITY: Incomplete
PR_SUBJECT: Incomplete
PR_SUBJECT_W: Incomplete
PR_SUBJECT_A: Incomplete
PR_SUBJECT_IPM: Incomplete
PR_CLIENT_SUBMIT_TIME: Incomplete
PR_REPORT_NAME: Incomplete
PR_REPORT_NAME_W: Incomplete
PR_REPORT_NAME_A: Incomplete
PR_SENT_REPRESENTING_SEARCH_KEY: Incomplete
PR_X400_CONTENT_TYPE: Incomplete
PR_SUBJECT_PREFIX: Incomplete
PR_SUBJECT_PREFIX_W: Incomplete
PR_SUBJECT_PREFIX_A: Incomplete
PR_NON_RECEIPT_REASON: Incomplete
PR_RECEIVED_BY_ENTRYID: Incomplete
PR_RECEIVED_BY_NAME: Incomplete
PR_RECEIVED_BY_NAME_W: Incomplete
PR_RECEIVED_BY_NAME_A: Incomplete
PR_SENT_REPRESENTING_ENTRYID: Incomplete
PR_SENT_REPRESENTING_NAME: Incomplete
PR_SENT_REPRESENTING_NAME_W: Incomplete
PR_SENT_REPRESENTING_NAME_A: Incomplete
PR_RCVD_REPRESENTING_ENTRYID: Incomplete
PR_RCVD_REPRESENTING_NAME: Incomplete
PR_RCVD_REPRESENTING_NAME_W: Incomplete
PR_RCVD_REPRESENTING_NAME_A: Incomplete
PR_REPORT_ENTRYID: Incomplete
PR_READ_RECEIPT_ENTRYID: Incomplete
PR_MESSAGE_SUBMISSION_ID: Incomplete
PR_PROVIDER_SUBMIT_TIME: Incomplete
PR_ORIGINAL_SUBJECT: Incomplete
PR_ORIGINAL_SUBJECT_W: Incomplete
PR_ORIGINAL_SUBJECT_A: Incomplete
PR_DISC_VAL: Incomplete
PR_ORIG_MESSAGE_CLASS: Incomplete
PR_ORIG_MESSAGE_CLASS_W: Incomplete
PR_ORIG_MESSAGE_CLASS_A: Incomplete
PR_ORIGINAL_AUTHOR_ENTRYID: Incomplete
PR_ORIGINAL_AUTHOR_NAME: Incomplete
PR_ORIGINAL_AUTHOR_NAME_W: Incomplete
PR_ORIGINAL_AUTHOR_NAME_A: Incomplete
PR_ORIGINAL_SUBMIT_TIME: Incomplete
PR_REPLY_RECIPIENT_ENTRIES: Incomplete
PR_REPLY_RECIPIENT_NAMES: Incomplete
PR_REPLY_RECIPIENT_NAMES_W: Incomplete
PR_REPLY_RECIPIENT_NAMES_A: Incomplete
PR_RECEIVED_BY_SEARCH_KEY: Incomplete
PR_RCVD_REPRESENTING_SEARCH_KEY: Incomplete
PR_READ_RECEIPT_SEARCH_KEY: Incomplete
PR_REPORT_SEARCH_KEY: Incomplete
PR_ORIGINAL_DELIVERY_TIME: Incomplete
PR_ORIGINAL_AUTHOR_SEARCH_KEY: Incomplete
PR_MESSAGE_TO_ME: Incomplete
PR_MESSAGE_CC_ME: Incomplete
PR_MESSAGE_RECIP_ME: Incomplete
PR_ORIGINAL_SENDER_NAME: Incomplete
PR_ORIGINAL_SENDER_NAME_W: Incomplete
PR_ORIGINAL_SENDER_NAME_A: Incomplete
PR_ORIGINAL_SENDER_ENTRYID: Incomplete
PR_ORIGINAL_SENDER_SEARCH_KEY: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_NAME: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_NAME_W: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_NAME_A: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_ENTRYID: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_SEARCH_KEY: Incomplete
PR_START_DATE: Incomplete
PR_END_DATE: Incomplete
PR_OWNER_APPT_ID: Incomplete
PR_RESPONSE_REQUESTED: Incomplete
PR_SENT_REPRESENTING_ADDRTYPE: Incomplete
PR_SENT_REPRESENTING_ADDRTYPE_W: Incomplete
PR_SENT_REPRESENTING_ADDRTYPE_A: Incomplete
PR_SENT_REPRESENTING_EMAIL_ADDRESS: Incomplete
PR_SENT_REPRESENTING_EMAIL_ADDRESS_W: Incomplete
PR_SENT_REPRESENTING_EMAIL_ADDRESS_A: Incomplete
PR_ORIGINAL_SENDER_ADDRTYPE: Incomplete
PR_ORIGINAL_SENDER_ADDRTYPE_W: Incomplete
PR_ORIGINAL_SENDER_ADDRTYPE_A: Incomplete
PR_ORIGINAL_SENDER_EMAIL_ADDRESS: Incomplete
PR_ORIGINAL_SENDER_EMAIL_ADDRESS_W: Incomplete
PR_ORIGINAL_SENDER_EMAIL_ADDRESS_A: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_ADDRTYPE: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_ADDRTYPE_W: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_ADDRTYPE_A: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_EMAIL_ADDRESS: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_EMAIL_ADDRESS_W: Incomplete
PR_ORIGINAL_SENT_REPRESENTING_EMAIL_ADDRESS_A: Incomplete
PR_CONVERSATION_TOPIC: Incomplete
PR_CONVERSATION_TOPIC_W: Incomplete
PR_CONVERSATION_TOPIC_A: Incomplete
PR_CONVERSATION_INDEX: Incomplete
PR_ORIGINAL_DISPLAY_BCC: Incomplete
PR_ORIGINAL_DISPLAY_BCC_W: Incomplete
PR_ORIGINAL_DISPLAY_BCC_A: Incomplete
PR_ORIGINAL_DISPLAY_CC: Incomplete
PR_ORIGINAL_DISPLAY_CC_W: Incomplete
PR_ORIGINAL_DISPLAY_CC_A: Incomplete
PR_ORIGINAL_DISPLAY_TO: Incomplete
PR_ORIGINAL_DISPLAY_TO_W: Incomplete
PR_ORIGINAL_DISPLAY_TO_A: Incomplete
PR_RECEIVED_BY_ADDRTYPE: Incomplete
PR_RECEIVED_BY_ADDRTYPE_W: Incomplete
PR_RECEIVED_BY_ADDRTYPE_A: Incomplete
PR_RECEIVED_BY_EMAIL_ADDRESS: Incomplete
PR_RECEIVED_BY_EMAIL_ADDRESS_W: Incomplete
PR_RECEIVED_BY_EMAIL_ADDRESS_A: Incomplete
PR_RCVD_REPRESENTING_ADDRTYPE: Incomplete
PR_RCVD_REPRESENTING_ADDRTYPE_W: Incomplete
PR_RCVD_REPRESENTING_ADDRTYPE_A: Incomplete
PR_RCVD_REPRESENTING_EMAIL_ADDRESS: Incomplete
PR_RCVD_REPRESENTING_EMAIL_ADDRESS_W: Incomplete
PR_RCVD_REPRESENTING_EMAIL_ADDRESS_A: Incomplete
PR_ORIGINAL_AUTHOR_ADDRTYPE: Incomplete
PR_ORIGINAL_AUTHOR_ADDRTYPE_W: Incomplete
PR_ORIGINAL_AUTHOR_ADDRTYPE_A: Incomplete
PR_ORIGINAL_AUTHOR_EMAIL_ADDRESS: Incomplete
PR_ORIGINAL_AUTHOR_EMAIL_ADDRESS_W: Incomplete
PR_ORIGINAL_AUTHOR_EMAIL_ADDRESS_A: Incomplete
PR_ORIGINALLY_INTENDED_RECIP_ADDRTYPE: Incomplete
PR_ORIGINALLY_INTENDED_RECIP_ADDRTYPE_W: Incomplete
PR_ORIGINALLY_INTENDED_RECIP_ADDRTYPE_A: Incomplete
PR_ORIGINALLY_INTENDED_RECIP_EMAIL_ADDRESS: Incomplete
PR_ORIGINALLY_INTENDED_RECIP_EMAIL_ADDRESS_W: Incomplete
PR_ORIGINALLY_INTENDED_RECIP_EMAIL_ADDRESS_A: Incomplete
PR_TRANSPORT_MESSAGE_HEADERS: Incomplete
PR_TRANSPORT_MESSAGE_HEADERS_W: Incomplete
PR_TRANSPORT_MESSAGE_HEADERS_A: Incomplete
PR_DELEGATION: Incomplete
PR_TNEF_CORRELATION_KEY: Incomplete
PR_BODY: Incomplete
PR_BODY_W: Incomplete
PR_BODY_A: Incomplete
PR_BODY_HTML: Incomplete
PR_BODY_HTML_W: Incomplete
PR_BODY_HTML_A: Incomplete
PR_REPORT_TEXT: Incomplete
PR_REPORT_TEXT_W: Incomplete
PR_REPORT_TEXT_A: Incomplete
PR_ORIGINATOR_AND_DL_EXPANSION_HISTORY: Incomplete
PR_REPORTING_DL_NAME: Incomplete
PR_REPORTING_MTA_CERTIFICATE: Incomplete
PR_RTF_SYNC_BODY_CRC: Incomplete
PR_RTF_SYNC_BODY_COUNT: Incomplete
PR_RTF_SYNC_BODY_TAG: Incomplete
PR_RTF_SYNC_BODY_TAG_W: Incomplete
PR_RTF_SYNC_BODY_TAG_A: Incomplete
PR_RTF_COMPRESSED: Incomplete
PR_RTF_SYNC_PREFIX_COUNT: Incomplete
PR_RTF_SYNC_TRAILING_COUNT: Incomplete
PR_ORIGINALLY_INTENDED_RECIP_ENTRYID: Incomplete
PR_CONTENT_INTEGRITY_CHECK: Incomplete
PR_EXPLICIT_CONVERSION: Incomplete
PR_IPM_RETURN_REQUESTED: Incomplete
PR_MESSAGE_TOKEN: Incomplete
PR_NDR_REASON_CODE: Incomplete
PR_NDR_DIAG_CODE: Incomplete
PR_NON_RECEIPT_NOTIFICATION_REQUESTED: Incomplete
PR_DELIVERY_POINT: Incomplete
PR_ORIGINATOR_NON_DELIVERY_REPORT_REQUESTED: Incomplete
PR_ORIGINATOR_REQUESTED_ALTERNATE_RECIPIENT: Incomplete
PR_PHYSICAL_DELIVERY_BUREAU_FAX_DELIVERY: Incomplete
PR_PHYSICAL_DELIVERY_MODE: Incomplete
PR_PHYSICAL_DELIVERY_REPORT_REQUEST: Incomplete
PR_PHYSICAL_FORWARDING_ADDRESS: Incomplete
PR_PHYSICAL_FORWARDING_ADDRESS_REQUESTED: Incomplete
PR_PHYSICAL_FORWARDING_PROHIBITED: Incomplete
PR_PHYSICAL_RENDITION_ATTRIBUTES: Incomplete
PR_PROOF_OF_DELIVERY: Incomplete
PR_PROOF_OF_DELIVERY_REQUESTED: Incomplete
PR_RECIPIENT_CERTIFICATE: Incomplete
PR_RECIPIENT_NUMBER_FOR_ADVICE: Incomplete
PR_RECIPIENT_NUMBER_FOR_ADVICE_W: Incomplete
PR_RECIPIENT_NUMBER_FOR_ADVICE_A: Incomplete
PR_RECIPIENT_TYPE: Incomplete
PR_REGISTERED_MAIL_TYPE: Incomplete
PR_REPLY_REQUESTED: Incomplete
PR_REQUESTED_DELIVERY_METHOD: Incomplete
PR_SENDER_ENTRYID: Incomplete
PR_SENDER_NAME: Incomplete
PR_SENDER_NAME_W: Incomplete
PR_SENDER_NAME_A: Incomplete
PR_SUPPLEMENTARY_INFO: Incomplete
PR_SUPPLEMENTARY_INFO_W: Incomplete
PR_SUPPLEMENTARY_INFO_A: Incomplete
PR_TYPE_OF_MTS_USER: Incomplete
PR_SENDER_SEARCH_KEY: Incomplete
PR_SENDER_ADDRTYPE: Incomplete
PR_SENDER_ADDRTYPE_W: Incomplete
PR_SENDER_ADDRTYPE_A: Incomplete
PR_SENDER_EMAIL_ADDRESS: Incomplete
PR_SENDER_EMAIL_ADDRESS_W: Incomplete
PR_SENDER_EMAIL_ADDRESS_A: Incomplete
PR_CURRENT_VERSION: Incomplete
PR_DELETE_AFTER_SUBMIT: Incomplete
PR_DISPLAY_BCC: Incomplete
PR_DISPLAY_BCC_W: Incomplete
PR_DISPLAY_BCC_A: Incomplete
PR_DISPLAY_CC: Incomplete
PR_DISPLAY_CC_W: Incomplete
PR_DISPLAY_CC_A: Incomplete
PR_DISPLAY_TO: Incomplete
PR_DISPLAY_TO_W: Incomplete
PR_DISPLAY_TO_A: Incomplete
PR_PARENT_DISPLAY: Incomplete
PR_PARENT_DISPLAY_W: Incomplete
PR_PARENT_DISPLAY_A: Incomplete
PR_MESSAGE_DELIVERY_TIME: Incomplete
PR_MESSAGE_FLAGS: Incomplete
PR_MESSAGE_SIZE: Incomplete
PR_PARENT_ENTRYID: Incomplete
PR_SENTMAIL_ENTRYID: Incomplete
PR_CORRELATE: Incomplete
PR_CORRELATE_MTSID: Incomplete
PR_DISCRETE_VALUES: Incomplete
PR_RESPONSIBILITY: Incomplete
PR_SPOOLER_STATUS: Incomplete
PR_TRANSPORT_STATUS: Incomplete
PR_MESSAGE_RECIPIENTS: Incomplete
PR_MESSAGE_ATTACHMENTS: Incomplete
PR_SUBMIT_FLAGS: Incomplete
PR_RECIPIENT_STATUS: Incomplete
PR_TRANSPORT_KEY: Incomplete
PR_MSG_STATUS: Incomplete
PR_MESSAGE_DOWNLOAD_TIME: Incomplete
PR_CREATION_VERSION: Incomplete
PR_MODIFY_VERSION: Incomplete
PR_HASATTACH: Incomplete
PR_BODY_CRC: Incomplete
PR_NORMALIZED_SUBJECT: Incomplete
PR_NORMALIZED_SUBJECT_W: Incomplete
PR_NORMALIZED_SUBJECT_A: Incomplete
PR_RTF_IN_SYNC: Incomplete
PR_ATTACH_SIZE: Incomplete
PR_ATTACH_NUM: Incomplete
PR_PREPROCESS: Incomplete
PR_ORIGINATING_MTA_CERTIFICATE: Incomplete
PR_PROOF_OF_SUBMISSION: Incomplete
PR_ENTRYID: Incomplete
PR_OBJECT_TYPE: Incomplete
PR_ICON: Incomplete
PR_MINI_ICON: Incomplete
PR_STORE_ENTRYID: Incomplete
PR_STORE_RECORD_KEY: Incomplete
PR_RECORD_KEY: Incomplete
PR_MAPPING_SIGNATURE: Incomplete
PR_ACCESS_LEVEL: Incomplete
PR_INSTANCE_KEY: Incomplete
PR_ROW_TYPE: Incomplete
PR_ACCESS: Incomplete
PR_ROWID: Incomplete
PR_DISPLAY_NAME: Incomplete
PR_DISPLAY_NAME_W: Incomplete
PR_DISPLAY_NAME_A: Incomplete
PR_ADDRTYPE: Incomplete
PR_ADDRTYPE_W: Incomplete
PR_ADDRTYPE_A: Incomplete
PR_EMAIL_ADDRESS: Incomplete
PR_EMAIL_ADDRESS_W: Incomplete
PR_EMAIL_ADDRESS_A: Incomplete
PR_COMMENT: Incomplete
PR_COMMENT_W: Incomplete
PR_COMMENT_A: Incomplete
PR_DEPTH: Incomplete
PR_PROVIDER_DISPLAY: Incomplete
PR_PROVIDER_DISPLAY_W: Incomplete
PR_PROVIDER_DISPLAY_A: Incomplete
PR_CREATION_TIME: Incomplete
PR_LAST_MODIFICATION_TIME: Incomplete
PR_RESOURCE_FLAGS: Incomplete
PR_PROVIDER_DLL_NAME: Incomplete
PR_PROVIDER_DLL_NAME_W: Incomplete
PR_PROVIDER_DLL_NAME_A: Incomplete
PR_SEARCH_KEY: Incomplete
PR_PROVIDER_UID: Incomplete
PR_PROVIDER_ORDINAL: Incomplete
PR_FORM_VERSION: Incomplete
PR_FORM_VERSION_W: Incomplete
PR_FORM_VERSION_A: Incomplete
PR_FORM_CLSID: Incomplete
PR_FORM_CONTACT_NAME: Incomplete
PR_FORM_CONTACT_NAME_W: Incomplete
PR_FORM_CONTACT_NAME_A: Incomplete
PR_FORM_CATEGORY: Incomplete
PR_FORM_CATEGORY_W: Incomplete
PR_FORM_CATEGORY_A: Incomplete
PR_FORM_CATEGORY_SUB: Incomplete
PR_FORM_CATEGORY_SUB_W: Incomplete
PR_FORM_CATEGORY_SUB_A: Incomplete
PR_FORM_HOST_MAP: Incomplete
PR_FORM_HIDDEN: Incomplete
PR_FORM_DESIGNER_NAME: Incomplete
PR_FORM_DESIGNER_NAME_W: Incomplete
PR_FORM_DESIGNER_NAME_A: Incomplete
PR_FORM_DESIGNER_GUID: Incomplete
PR_FORM_MESSAGE_BEHAVIOR: Incomplete
PR_DEFAULT_STORE: Incomplete
PR_STORE_SUPPORT_MASK: Incomplete
PR_STORE_STATE: Incomplete
PR_IPM_SUBTREE_SEARCH_KEY: Incomplete
PR_IPM_OUTBOX_SEARCH_KEY: Incomplete
PR_IPM_WASTEBASKET_SEARCH_KEY: Incomplete
PR_IPM_SENTMAIL_SEARCH_KEY: Incomplete
PR_MDB_PROVIDER: Incomplete
PR_RECEIVE_FOLDER_SETTINGS: Incomplete
PR_VALID_FOLDER_MASK: Incomplete
PR_IPM_SUBTREE_ENTRYID: Incomplete
PR_IPM_OUTBOX_ENTRYID: Incomplete
PR_IPM_WASTEBASKET_ENTRYID: Incomplete
PR_IPM_SENTMAIL_ENTRYID: Incomplete
PR_VIEWS_ENTRYID: Incomplete
PR_COMMON_VIEWS_ENTRYID: Incomplete
PR_FINDER_ENTRYID: Incomplete
PR_CONTAINER_FLAGS: Incomplete
PR_FOLDER_TYPE: Incomplete
PR_CONTENT_COUNT: Incomplete
PR_CONTENT_UNREAD: Incomplete
PR_CREATE_TEMPLATES: Incomplete
PR_DETAILS_TABLE: Incomplete
PR_SEARCH: Incomplete
PR_SELECTABLE: Incomplete
PR_SUBFOLDERS: Incomplete
PR_STATUS: Incomplete
PR_ANR: Incomplete
PR_ANR_W: Incomplete
PR_ANR_A: Incomplete
PR_CONTENTS_SORT_ORDER: Incomplete
PR_CONTAINER_HIERARCHY: Incomplete
PR_CONTAINER_CONTENTS: Incomplete
PR_FOLDER_ASSOCIATED_CONTENTS: Incomplete
PR_DEF_CREATE_DL: Incomplete
PR_DEF_CREATE_MAILUSER: Incomplete
PR_CONTAINER_CLASS: Incomplete
PR_CONTAINER_CLASS_W: Incomplete
PR_CONTAINER_CLASS_A: Incomplete
PR_CONTAINER_MODIFY_VERSION: Incomplete
PR_AB_PROVIDER_ID: Incomplete
PR_DEFAULT_VIEW_ENTRYID: Incomplete
PR_ASSOC_CONTENT_COUNT: Incomplete
PR_ATTACHMENT_X400_PARAMETERS: Incomplete
PR_ATTACH_DATA_OBJ: Incomplete
PR_ATTACH_DATA_BIN: Incomplete
PR_ATTACH_ENCODING: Incomplete
PR_ATTACH_EXTENSION: Incomplete
PR_ATTACH_EXTENSION_W: Incomplete
PR_ATTACH_EXTENSION_A: Incomplete
PR_ATTACH_FILENAME: Incomplete
PR_ATTACH_FILENAME_W: Incomplete
PR_ATTACH_FILENAME_A: Incomplete
PR_ATTACH_METHOD: Incomplete
PR_ATTACH_LONG_FILENAME: Incomplete
PR_ATTACH_LONG_FILENAME_W: Incomplete
PR_ATTACH_LONG_FILENAME_A: Incomplete
PR_ATTACH_PATHNAME: Incomplete
PR_ATTACH_PATHNAME_W: Incomplete
PR_ATTACH_PATHNAME_A: Incomplete
PR_ATTACH_RENDERING: Incomplete
PR_ATTACH_TAG: Incomplete
PR_RENDERING_POSITION: Incomplete
PR_ATTACH_TRANSPORT_NAME: Incomplete
PR_ATTACH_TRANSPORT_NAME_W: Incomplete
PR_ATTACH_TRANSPORT_NAME_A: Incomplete
PR_ATTACH_LONG_PATHNAME: Incomplete
PR_ATTACH_LONG_PATHNAME_W: Incomplete
PR_ATTACH_LONG_PATHNAME_A: Incomplete
PR_ATTACH_MIME_TAG: Incomplete
PR_ATTACH_MIME_TAG_W: Incomplete
PR_ATTACH_MIME_TAG_A: Incomplete
PR_ATTACH_ADDITIONAL_INFO: Incomplete
PR_DISPLAY_TYPE: Incomplete
PR_TEMPLATEID: Incomplete
PR_PRIMARY_CAPABILITY: Incomplete
PR_7BIT_DISPLAY_NAME: Incomplete
PR_ACCOUNT: Incomplete
PR_ACCOUNT_W: Incomplete
PR_ACCOUNT_A: Incomplete
PR_ALTERNATE_RECIPIENT: Incomplete
PR_CALLBACK_TELEPHONE_NUMBER: Incomplete
PR_CALLBACK_TELEPHONE_NUMBER_W: Incomplete
PR_CALLBACK_TELEPHONE_NUMBER_A: Incomplete
PR_CONVERSION_PROHIBITED: Incomplete
PR_DISCLOSE_RECIPIENTS: Incomplete
PR_GENERATION: Incomplete
PR_GENERATION_W: Incomplete
PR_GENERATION_A: Incomplete
PR_GIVEN_NAME: Incomplete
PR_GIVEN_NAME_W: Incomplete
PR_GIVEN_NAME_A: Incomplete
PR_GOVERNMENT_ID_NUMBER: Incomplete
PR_GOVERNMENT_ID_NUMBER_W: Incomplete
PR_GOVERNMENT_ID_NUMBER_A: Incomplete
PR_BUSINESS_TELEPHONE_NUMBER: Incomplete
PR_BUSINESS_TELEPHONE_NUMBER_W: Incomplete
PR_BUSINESS_TELEPHONE_NUMBER_A: Incomplete
PR_OFFICE_TELEPHONE_NUMBER: Incomplete
PR_OFFICE_TELEPHONE_NUMBER_W: Incomplete
PR_OFFICE_TELEPHONE_NUMBER_A: Incomplete
PR_HOME_TELEPHONE_NUMBER: Incomplete
PR_HOME_TELEPHONE_NUMBER_W: Incomplete
PR_HOME_TELEPHONE_NUMBER_A: Incomplete
PR_INITIALS: Incomplete
PR_INITIALS_W: Incomplete
PR_INITIALS_A: Incomplete
PR_KEYWORD: Incomplete
PR_KEYWORD_W: Incomplete
PR_KEYWORD_A: Incomplete
PR_LANGUAGE: Incomplete
PR_LANGUAGE_W: Incomplete
PR_LANGUAGE_A: Incomplete
PR_LOCATION: Incomplete
PR_LOCATION_W: Incomplete
PR_LOCATION_A: Incomplete
PR_MAIL_PERMISSION: Incomplete
PR_MHS_COMMON_NAME: Incomplete
PR_MHS_COMMON_NAME_W: Incomplete
PR_MHS_COMMON_NAME_A: Incomplete
PR_ORGANIZATIONAL_ID_NUMBER: Incomplete
PR_ORGANIZATIONAL_ID_NUMBER_W: Incomplete
PR_ORGANIZATIONAL_ID_NUMBER_A: Incomplete
PR_SURNAME: Incomplete
PR_SURNAME_W: Incomplete
PR_SURNAME_A: Incomplete
PR_ORIGINAL_ENTRYID: Incomplete
PR_ORIGINAL_DISPLAY_NAME: Incomplete
PR_ORIGINAL_DISPLAY_NAME_W: Incomplete
PR_ORIGINAL_DISPLAY_NAME_A: Incomplete
PR_ORIGINAL_SEARCH_KEY: Incomplete
PR_POSTAL_ADDRESS: Incomplete
PR_POSTAL_ADDRESS_W: Incomplete
PR_POSTAL_ADDRESS_A: Incomplete
PR_COMPANY_NAME: Incomplete
PR_COMPANY_NAME_W: Incomplete
PR_COMPANY_NAME_A: Incomplete
PR_TITLE: Incomplete
PR_TITLE_W: Incomplete
PR_TITLE_A: Incomplete
PR_DEPARTMENT_NAME: Incomplete
PR_DEPARTMENT_NAME_W: Incomplete
PR_DEPARTMENT_NAME_A: Incomplete
PR_OFFICE_LOCATION: Incomplete
PR_OFFICE_LOCATION_W: Incomplete
PR_OFFICE_LOCATION_A: Incomplete
PR_PRIMARY_TELEPHONE_NUMBER: Incomplete
PR_PRIMARY_TELEPHONE_NUMBER_W: Incomplete
PR_PRIMARY_TELEPHONE_NUMBER_A: Incomplete
PR_BUSINESS2_TELEPHONE_NUMBER: Incomplete
PR_BUSINESS2_TELEPHONE_NUMBER_W: Incomplete
PR_BUSINESS2_TELEPHONE_NUMBER_A: Incomplete
PR_OFFICE2_TELEPHONE_NUMBER: Incomplete
PR_OFFICE2_TELEPHONE_NUMBER_W: Incomplete
PR_OFFICE2_TELEPHONE_NUMBER_A: Incomplete
PR_MOBILE_TELEPHONE_NUMBER: Incomplete
PR_MOBILE_TELEPHONE_NUMBER_W: Incomplete
PR_MOBILE_TELEPHONE_NUMBER_A: Incomplete
PR_CELLULAR_TELEPHONE_NUMBER: Incomplete
PR_CELLULAR_TELEPHONE_NUMBER_W: Incomplete
PR_CELLULAR_TELEPHONE_NUMBER_A: Incomplete
PR_RADIO_TELEPHONE_NUMBER: Incomplete
PR_RADIO_TELEPHONE_NUMBER_W: Incomplete
PR_RADIO_TELEPHONE_NUMBER_A: Incomplete
PR_CAR_TELEPHONE_NUMBER: Incomplete
PR_CAR_TELEPHONE_NUMBER_W: Incomplete
PR_CAR_TELEPHONE_NUMBER_A: Incomplete
PR_OTHER_TELEPHONE_NUMBER: Incomplete
PR_OTHER_TELEPHONE_NUMBER_W: Incomplete
PR_OTHER_TELEPHONE_NUMBER_A: Incomplete
PR_TRANSMITABLE_DISPLAY_NAME: Incomplete
PR_TRANSMITABLE_DISPLAY_NAME_W: Incomplete
PR_TRANSMITABLE_DISPLAY_NAME_A: Incomplete
PR_PAGER_TELEPHONE_NUMBER: Incomplete
PR_PAGER_TELEPHONE_NUMBER_W: Incomplete
PR_PAGER_TELEPHONE_NUMBER_A: Incomplete
PR_BEEPER_TELEPHONE_NUMBER: Incomplete
PR_BEEPER_TELEPHONE_NUMBER_W: Incomplete
PR_BEEPER_TELEPHONE_NUMBER_A: Incomplete
PR_USER_CERTIFICATE: Incomplete
PR_PRIMARY_FAX_NUMBER: Incomplete
PR_PRIMARY_FAX_NUMBER_W: Incomplete
PR_PRIMARY_FAX_NUMBER_A: Incomplete
PR_BUSINESS_FAX_NUMBER: Incomplete
PR_BUSINESS_FAX_NUMBER_W: Incomplete
PR_BUSINESS_FAX_NUMBER_A: Incomplete
PR_HOME_FAX_NUMBER: Incomplete
PR_HOME_FAX_NUMBER_W: Incomplete
PR_HOME_FAX_NUMBER_A: Incomplete
PR_COUNTRY: Incomplete
PR_COUNTRY_W: Incomplete
PR_COUNTRY_A: Incomplete
PR_BUSINESS_ADDRESS_COUNTRY: Incomplete
PR_BUSINESS_ADDRESS_COUNTRY_W: Incomplete
PR_BUSINESS_ADDRESS_COUNTRY_A: Incomplete
PR_LOCALITY: Incomplete
PR_LOCALITY_W: Incomplete
PR_LOCALITY_A: Incomplete
PR_BUSINESS_ADDRESS_CITY: Incomplete
PR_BUSINESS_ADDRESS_CITY_W: Incomplete
PR_BUSINESS_ADDRESS_CITY_A: Incomplete
PR_STATE_OR_PROVINCE: Incomplete
PR_STATE_OR_PROVINCE_W: Incomplete
PR_STATE_OR_PROVINCE_A: Incomplete
PR_BUSINESS_ADDRESS_STATE_OR_PROVINCE: Incomplete
PR_BUSINESS_ADDRESS_STATE_OR_PROVINCE_W: Incomplete
PR_BUSINESS_ADDRESS_STATE_OR_PROVINCE_A: Incomplete
PR_STREET_ADDRESS: Incomplete
PR_STREET_ADDRESS_W: Incomplete
PR_STREET_ADDRESS_A: Incomplete
PR_BUSINESS_ADDRESS_STREET: Incomplete
PR_BUSINESS_ADDRESS_STREET_W: Incomplete
PR_BUSINESS_ADDRESS_STREET_A: Incomplete
PR_POSTAL_CODE: Incomplete
PR_POSTAL_CODE_W: Incomplete
PR_POSTAL_CODE_A: Incomplete
PR_BUSINESS_ADDRESS_POSTAL_CODE: Incomplete
PR_BUSINESS_ADDRESS_POSTAL_CODE_W: Incomplete
PR_BUSINESS_ADDRESS_POSTAL_CODE_A: Incomplete
PR_POST_OFFICE_BOX: Incomplete
PR_POST_OFFICE_BOX_W: Incomplete
PR_POST_OFFICE_BOX_A: Incomplete
PR_BUSINESS_ADDRESS_POST_OFFICE_BOX: Incomplete
PR_BUSINESS_ADDRESS_POST_OFFICE_BOX_W: Incomplete
PR_BUSINESS_ADDRESS_POST_OFFICE_BOX_A: Incomplete
PR_TELEX_NUMBER: Incomplete
PR_TELEX_NUMBER_W: Incomplete
PR_TELEX_NUMBER_A: Incomplete
PR_ISDN_NUMBER: Incomplete
PR_ISDN_NUMBER_W: Incomplete
PR_ISDN_NUMBER_A: Incomplete
PR_ASSISTANT_TELEPHONE_NUMBER: Incomplete
PR_ASSISTANT_TELEPHONE_NUMBER_W: Incomplete
PR_ASSISTANT_TELEPHONE_NUMBER_A: Incomplete
PR_HOME2_TELEPHONE_NUMBER: Incomplete
PR_HOME2_TELEPHONE_NUMBER_W: Incomplete
PR_HOME2_TELEPHONE_NUMBER_A: Incomplete
PR_ASSISTANT: Incomplete
PR_ASSISTANT_W: Incomplete
PR_ASSISTANT_A: Incomplete
PR_SEND_RICH_INFO: Incomplete
PR_WEDDING_ANNIVERSARY: Incomplete
PR_BIRTHDAY: Incomplete
PR_HOBBIES: Incomplete
PR_HOBBIES_W: Incomplete
PR_HOBBIES_A: Incomplete
PR_MIDDLE_NAME: Incomplete
PR_MIDDLE_NAME_W: Incomplete
PR_MIDDLE_NAME_A: Incomplete
PR_DISPLAY_NAME_PREFIX: Incomplete
PR_DISPLAY_NAME_PREFIX_W: Incomplete
PR_DISPLAY_NAME_PREFIX_A: Incomplete
PR_PROFESSION: Incomplete
PR_PROFESSION_W: Incomplete
PR_PROFESSION_A: Incomplete
PR_PREFERRED_BY_NAME: Incomplete
PR_PREFERRED_BY_NAME_W: Incomplete
PR_PREFERRED_BY_NAME_A: Incomplete
PR_SPOUSE_NAME: Incomplete
PR_SPOUSE_NAME_W: Incomplete
PR_SPOUSE_NAME_A: Incomplete
PR_COMPUTER_NETWORK_NAME: Incomplete
PR_COMPUTER_NETWORK_NAME_W: Incomplete
PR_COMPUTER_NETWORK_NAME_A: Incomplete
PR_CUSTOMER_ID: Incomplete
PR_CUSTOMER_ID_W: Incomplete
PR_CUSTOMER_ID_A: Incomplete
PR_TTYTDD_PHONE_NUMBER: Incomplete
PR_TTYTDD_PHONE_NUMBER_W: Incomplete
PR_TTYTDD_PHONE_NUMBER_A: Incomplete
PR_FTP_SITE: Incomplete
PR_FTP_SITE_W: Incomplete
PR_FTP_SITE_A: Incomplete
PR_GENDER: Incomplete
PR_MANAGER_NAME: Incomplete
PR_MANAGER_NAME_W: Incomplete
PR_MANAGER_NAME_A: Incomplete
PR_NICKNAME: Incomplete
PR_NICKNAME_W: Incomplete
PR_NICKNAME_A: Incomplete
PR_PERSONAL_HOME_PAGE: Incomplete
PR_PERSONAL_HOME_PAGE_W: Incomplete
PR_PERSONAL_HOME_PAGE_A: Incomplete
PR_BUSINESS_HOME_PAGE: Incomplete
PR_BUSINESS_HOME_PAGE_W: Incomplete
PR_BUSINESS_HOME_PAGE_A: Incomplete
PR_CONTACT_VERSION: Incomplete
PR_CONTACT_ENTRYIDS: Incomplete
PR_CONTACT_ADDRTYPES: Incomplete
PR_CONTACT_ADDRTYPES_W: Incomplete
PR_CONTACT_ADDRTYPES_A: Incomplete
PR_CONTACT_DEFAULT_ADDRESS_INDEX: Incomplete
PR_CONTACT_EMAIL_ADDRESSES: Incomplete
PR_CONTACT_EMAIL_ADDRESSES_W: Incomplete
PR_CONTACT_EMAIL_ADDRESSES_A: Incomplete
PR_COMPANY_MAIN_PHONE_NUMBER: Incomplete
PR_COMPANY_MAIN_PHONE_NUMBER_W: Incomplete
PR_COMPANY_MAIN_PHONE_NUMBER_A: Incomplete
PR_CHILDRENS_NAMES: Incomplete
PR_CHILDRENS_NAMES_W: Incomplete
PR_CHILDRENS_NAMES_A: Incomplete
PR_HOME_ADDRESS_CITY: Incomplete
PR_HOME_ADDRESS_CITY_W: Incomplete
PR_HOME_ADDRESS_CITY_A: Incomplete
PR_HOME_ADDRESS_COUNTRY: Incomplete
PR_HOME_ADDRESS_COUNTRY_W: Incomplete
PR_HOME_ADDRESS_COUNTRY_A: Incomplete
PR_HOME_ADDRESS_POSTAL_CODE: Incomplete
PR_HOME_ADDRESS_POSTAL_CODE_W: Incomplete
PR_HOME_ADDRESS_POSTAL_CODE_A: Incomplete
PR_HOME_ADDRESS_STATE_OR_PROVINCE: Incomplete
PR_HOME_ADDRESS_STATE_OR_PROVINCE_W: Incomplete
PR_HOME_ADDRESS_STATE_OR_PROVINCE_A: Incomplete
PR_HOME_ADDRESS_STREET: Incomplete
PR_HOME_ADDRESS_STREET_W: Incomplete
PR_HOME_ADDRESS_STREET_A: Incomplete
PR_HOME_ADDRESS_POST_OFFICE_BOX: Incomplete
PR_HOME_ADDRESS_POST_OFFICE_BOX_W: Incomplete
PR_HOME_ADDRESS_POST_OFFICE_BOX_A: Incomplete
PR_OTHER_ADDRESS_CITY: Incomplete
PR_OTHER_ADDRESS_CITY_W: Incomplete
PR_OTHER_ADDRESS_CITY_A: Incomplete
PR_OTHER_ADDRESS_COUNTRY: Incomplete
PR_OTHER_ADDRESS_COUNTRY_W: Incomplete
PR_OTHER_ADDRESS_COUNTRY_A: Incomplete
PR_OTHER_ADDRESS_POSTAL_CODE: Incomplete
PR_OTHER_ADDRESS_POSTAL_CODE_W: Incomplete
PR_OTHER_ADDRESS_POSTAL_CODE_A: Incomplete
PR_OTHER_ADDRESS_STATE_OR_PROVINCE: Incomplete
PR_OTHER_ADDRESS_STATE_OR_PROVINCE_W: Incomplete
PR_OTHER_ADDRESS_STATE_OR_PROVINCE_A: Incomplete
PR_OTHER_ADDRESS_STREET: Incomplete
PR_OTHER_ADDRESS_STREET_W: Incomplete
PR_OTHER_ADDRESS_STREET_A: Incomplete
PR_OTHER_ADDRESS_POST_OFFICE_BOX: Incomplete
PR_OTHER_ADDRESS_POST_OFFICE_BOX_W: Incomplete
PR_OTHER_ADDRESS_POST_OFFICE_BOX_A: Incomplete
PR_STORE_PROVIDERS: Incomplete
PR_AB_PROVIDERS: Incomplete
PR_TRANSPORT_PROVIDERS: Incomplete
PR_DEFAULT_PROFILE: Incomplete
PR_AB_SEARCH_PATH: Incomplete
PR_AB_DEFAULT_DIR: Incomplete
PR_AB_DEFAULT_PAB: Incomplete
PR_FILTERING_HOOKS: Incomplete
PR_SERVICE_NAME: Incomplete
PR_SERVICE_NAME_W: Incomplete
PR_SERVICE_NAME_A: Incomplete
PR_SERVICE_DLL_NAME: Incomplete
PR_SERVICE_DLL_NAME_W: Incomplete
PR_SERVICE_DLL_NAME_A: Incomplete
PR_SERVICE_ENTRY_NAME: Incomplete
PR_SERVICE_UID: Incomplete
PR_SERVICE_EXTRA_UIDS: Incomplete
PR_SERVICES: Incomplete
PR_SERVICE_SUPPORT_FILES: Incomplete
PR_SERVICE_SUPPORT_FILES_W: Incomplete
PR_SERVICE_SUPPORT_FILES_A: Incomplete
PR_SERVICE_DELETE_FILES: Incomplete
PR_SERVICE_DELETE_FILES_W: Incomplete
PR_SERVICE_DELETE_FILES_A: Incomplete
PR_AB_SEARCH_PATH_UPDATE: Incomplete
PR_PROFILE_NAME: Incomplete
PR_PROFILE_NAME_A: Incomplete
PR_PROFILE_NAME_W: Incomplete
PR_IDENTITY_DISPLAY: Incomplete
PR_IDENTITY_DISPLAY_W: Incomplete
PR_IDENTITY_DISPLAY_A: Incomplete
PR_IDENTITY_ENTRYID: Incomplete
PR_RESOURCE_METHODS: Incomplete
PR_RESOURCE_TYPE: Incomplete
PR_STATUS_CODE: Incomplete
PR_IDENTITY_SEARCH_KEY: Incomplete
PR_OWN_STORE_ENTRYID: Incomplete
PR_RESOURCE_PATH: Incomplete
PR_RESOURCE_PATH_W: Incomplete
PR_RESOURCE_PATH_A: Incomplete
PR_STATUS_STRING: Incomplete
PR_STATUS_STRING_W: Incomplete
PR_STATUS_STRING_A: Incomplete
PR_X400_DEFERRED_DELIVERY_CANCEL: Incomplete
PR_HEADER_FOLDER_ENTRYID: Incomplete
PR_REMOTE_PROGRESS: Incomplete
PR_REMOTE_PROGRESS_TEXT: Incomplete
PR_REMOTE_PROGRESS_TEXT_W: Incomplete
PR_REMOTE_PROGRESS_TEXT_A: Incomplete
PR_REMOTE_VALIDATE_OK: Incomplete
PR_CONTROL_FLAGS: Incomplete
PR_CONTROL_STRUCTURE: Incomplete
PR_CONTROL_TYPE: Incomplete
PR_DELTAX: Incomplete
PR_DELTAY: Incomplete
PR_XPOS: Incomplete
PR_YPOS: Incomplete
PR_CONTROL_ID: Incomplete
PR_INITIAL_DETAILS_PANE: Incomplete
PROP_ID_SECURE_MIN: int
PROP_ID_SECURE_MAX: int
pidExchangeXmitReservedMin: int
pidExchangeNonXmitReservedMin: int
pidProfileMin: int
pidStoreMin: int
pidFolderMin: int
pidMessageReadOnlyMin: int
pidMessageWriteableMin: int
pidAttachReadOnlyMin: int
pidSpecialMin: int
pidAdminMin: int
pidSecureProfileMin: int
PR_PROFILE_VERSION: Incomplete
PR_PROFILE_CONFIG_FLAGS: Incomplete
PR_PROFILE_HOME_SERVER: Incomplete
PR_PROFILE_HOME_SERVER_DN: Incomplete
PR_PROFILE_HOME_SERVER_ADDRS: Incomplete
PR_PROFILE_USER: Incomplete
PR_PROFILE_CONNECT_FLAGS: Incomplete
PR_PROFILE_TRANSPORT_FLAGS: Incomplete
PR_PROFILE_UI_STATE: Incomplete
PR_PROFILE_UNRESOLVED_NAME: Incomplete
PR_PROFILE_UNRESOLVED_SERVER: Incomplete
PR_PROFILE_BINDING_ORDER: Incomplete
PR_PROFILE_MAX_RESTRICT: Incomplete
PR_PROFILE_AB_FILES_PATH: Incomplete
PR_PROFILE_OFFLINE_STORE_PATH: Incomplete
PR_PROFILE_OFFLINE_INFO: Incomplete
PR_PROFILE_ADDR_INFO: Incomplete
PR_PROFILE_OPTIONS_DATA: Incomplete
PR_PROFILE_SECURE_MAILBOX: Incomplete
PR_DISABLE_WINSOCK: Incomplete
PR_OST_ENCRYPTION: Incomplete
PR_PROFILE_OPEN_FLAGS: Incomplete
PR_PROFILE_TYPE: Incomplete
PR_PROFILE_MAILBOX: Incomplete
PR_PROFILE_SERVER: Incomplete
PR_PROFILE_SERVER_DN: Incomplete
PR_PROFILE_FAVFLD_DISPLAY_NAME: Incomplete
PR_PROFILE_FAVFLD_COMMENT: Incomplete
PR_PROFILE_ALLPUB_DISPLAY_NAME: Incomplete
PR_PROFILE_ALLPUB_COMMENT: Incomplete
OSTF_NO_ENCRYPTION: int
OSTF_COMPRESSABLE_ENCRYPTION: int
OSTF_BEST_ENCRYPTION: int
PR_NON_IPM_SUBTREE_ENTRYID: Incomplete
PR_EFORMS_REGISTRY_ENTRYID: Incomplete
PR_SPLUS_FREE_BUSY_ENTRYID: Incomplete
PR_OFFLINE_ADDRBOOK_ENTRYID: Incomplete
PR_EFORMS_FOR_LOCALE_ENTRYID: Incomplete
PR_FREE_BUSY_FOR_LOCAL_SITE_ENTRYID: Incomplete
PR_ADDRBOOK_FOR_LOCAL_SITE_ENTRYID: Incomplete
PR_OFFLINE_MESSAGE_ENTRYID: Incomplete
PR_IPM_FAVORITES_ENTRYID: Incomplete
PR_IPM_PUBLIC_FOLDERS_ENTRYID: Incomplete
PR_GW_MTSIN_ENTRYID: Incomplete
PR_GW_MTSOUT_ENTRYID: Incomplete
PR_TRANSFER_ENABLED: Incomplete
PR_TEST_LINE_SPEED: Incomplete
PR_HIERARCHY_SYNCHRONIZER: Incomplete
PR_CONTENTS_SYNCHRONIZER: Incomplete
PR_COLLECTOR: Incomplete
PR_FAST_TRANSFER: Incomplete
PR_STORE_OFFLINE: Incomplete
PR_IN_TRANSIT: Incomplete
PR_REPLICATION_STYLE: Incomplete
PR_REPLICATION_SCHEDULE: Incomplete
PR_REPLICATION_MESSAGE_PRIORITY: Incomplete
PR_OVERALL_MSG_AGE_LIMIT: Incomplete
PR_REPLICATION_ALWAYS_INTERVAL: Incomplete
PR_REPLICATION_MSG_SIZE: Incomplete
STYLE_ALWAYS_INTERVAL_DEFAULT: int
REPLICATION_MESSAGE_SIZE_LIMIT_DEFAULT: int
STYLE_NEVER: int
STYLE_NORMAL: int
STYLE_ALWAYS: int
STYLE_DEFAULT: int
PR_SOURCE_KEY: Incomplete
PR_PARENT_SOURCE_KEY: Incomplete
PR_CHANGE_KEY: Incomplete
PR_PREDECESSOR_CHANGE_LIST: Incomplete
PR_FOLDER_CHILD_COUNT: Incomplete
PR_RIGHTS: Incomplete
PR_ACL_TABLE: Incomplete
PR_RULES_TABLE: Incomplete
PR_HAS_RULES: Incomplete
PR_ADDRESS_BOOK_ENTRYID: Incomplete
PR_ACL_DATA: Incomplete
PR_RULES_DATA: Incomplete
PR_FOLDER_DESIGN_FLAGS: Incomplete
PR_DESIGN_IN_PROGRESS: Incomplete
PR_SECURE_ORIGINATION: Incomplete
PR_PUBLISH_IN_ADDRESS_BOOK: Incomplete
PR_RESOLVE_METHOD: Incomplete
PR_ADDRESS_BOOK_DISPLAY_NAME: Incomplete
PR_EFORMS_LOCALE_ID: Incomplete
PR_REPLICA_LIST: Incomplete
PR_OVERALL_AGE_LIMIT: Incomplete
RESOLVE_METHOD_DEFAULT: int
RESOLVE_METHOD_LAST_WRITER_WINS: int
RESOLVE_METHOD_NO_CONFLICT_NOTIFICATION: int
PR_PUBLIC_FOLDER_ENTRYID: Incomplete
PR_HAS_NAMED_PROPERTIES: Incomplete
PR_CREATOR_NAME: Incomplete
PR_CREATOR_ENTRYID: Incomplete
PR_LAST_MODIFIER_NAME: Incomplete
PR_LAST_MODIFIER_ENTRYID: Incomplete
PR_HAS_DAMS: Incomplete
PR_RULE_TRIGGER_HISTORY: Incomplete
PR_MOVE_TO_STORE_ENTRYID: Incomplete
PR_MOVE_TO_FOLDER_ENTRYID: Incomplete
PR_REPLICA_SERVER: Incomplete
PR_DEFERRED_SEND_NUMBER: Incomplete
PR_DEFERRED_SEND_UNITS: Incomplete
PR_EXPIRY_NUMBER: Incomplete
PR_EXPIRY_UNITS: Incomplete
PR_DEFERRED_SEND_TIME: Incomplete
PR_GW_ADMIN_OPERATIONS: Incomplete
PR_P1_CONTENT: Incomplete
PR_P1_CONTENT_TYPE: Incomplete
PR_CLIENT_ACTIONS: Incomplete
PR_DAM_ORIGINAL_ENTRYID: Incomplete
PR_DAM_BACK_PATCHED: Incomplete
PR_RULE_ERROR: Incomplete
PR_RULE_ACTION_TYPE: Incomplete
PR_RULE_ACTION_NUMBER: Incomplete
PR_RULE_FOLDER_ENTRYID: Incomplete
PR_CONFLICT_ENTRYID: Incomplete
PR_MESSAGE_LOCALE_ID: Incomplete
PR_STORAGE_QUOTA_LIMIT: Incomplete
PR_EXCESS_STORAGE_USED: Incomplete
PR_SVR_GENERATING_QUOTA_MSG: Incomplete
PR_DELEGATED_BY_RULE: Incomplete
MSGSTATUS_IN_CONFLICT: int
PR_IN_CONFLICT: Incomplete
PR_LONGTERM_ENTRYID_FROM_TABLE: Incomplete
PR_ORIGINATOR_NAME: Incomplete
PR_ORIGINATOR_ADDR: Incomplete
PR_ORIGINATOR_ADDRTYPE: Incomplete
PR_ORIGINATOR_ENTRYID: Incomplete
PR_ARRIVAL_TIME: Incomplete
PR_TRACE_INFO: Incomplete
PR_INTERNAL_TRACE_INFO: Incomplete
PR_SUBJECT_TRACE_INFO: Incomplete
PR_RECIPIENT_NUMBER: Incomplete
PR_MTS_SUBJECT_ID: Incomplete
PR_REPORT_DESTINATION_NAME: Incomplete
PR_REPORT_DESTINATION_ENTRYID: Incomplete
PR_CONTENT_SEARCH_KEY: Incomplete
PR_FOREIGN_ID: Incomplete
PR_FOREIGN_REPORT_ID: Incomplete
PR_FOREIGN_SUBJECT_ID: Incomplete
PR_MTS_ID: Incomplete
PR_MTS_REPORT_ID: Incomplete
PR_FOLDER_FLAGS: Incomplete
PR_LAST_ACCESS_TIME: Incomplete
PR_RESTRICTION_COUNT: Incomplete
PR_CATEG_COUNT: Incomplete
PR_CACHED_COLUMN_COUNT: Incomplete
PR_NORMAL_MSG_W_ATTACH_COUNT: Incomplete
PR_ASSOC_MSG_W_ATTACH_COUNT: Incomplete
PR_RECIPIENT_ON_NORMAL_MSG_COUNT: Incomplete
PR_RECIPIENT_ON_ASSOC_MSG_COUNT: Incomplete
PR_ATTACH_ON_NORMAL_MSG_COUNT: Incomplete
PR_ATTACH_ON_ASSOC_MSG_COUNT: Incomplete
PR_NORMAL_MESSAGE_SIZE: Incomplete
PR_NORMAL_MESSAGE_SIZE_EXTENDED: Incomplete
PR_ASSOC_MESSAGE_SIZE: Incomplete
PR_ASSOC_MESSAGE_SIZE_EXTENDED: Incomplete
PR_FOLDER_PATHNAME: Incomplete
PR_OWNER_COUNT: Incomplete
PR_CONTACT_COUNT: Incomplete
PR_MESSAGE_SIZE_EXTENDED: Incomplete
PR_USERFIELDS: Incomplete
PR_FORCE_USE_ENTRYID_SERVER: Incomplete
PR_PROFILE_MDB_DN: Incomplete
PST_EXTERN_PROPID_BASE: int
PR_PST_PATH: Incomplete
PR_PST_PATH_W: Incomplete
PR_PST_PATH_A: Incomplete
PR_PST_REMEMBER_PW: Incomplete
PR_PST_ENCRYPTION: Incomplete
PR_PST_PW_SZ_OLD: Incomplete
PR_PST_PW_SZ_OLD_W: Incomplete
PR_PST_PW_SZ_OLD_A: Incomplete
PR_PST_PW_SZ_NEW: Incomplete
PR_PST_PW_SZ_NEW_W: Incomplete
PR_PST_PW_SZ_NEW_A: Incomplete
