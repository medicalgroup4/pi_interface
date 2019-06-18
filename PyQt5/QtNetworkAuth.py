# encoding: utf-8
# module PyQt5.QtNetworkAuth
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtNetworkAuth.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QAbstractOAuth(__PyQt5_QtCore.QObject):
    # no doc
    def authorizationUrl(self): # real signature unknown; restored from __doc__
        """ authorizationUrl(self) -> QUrl """
        pass

    def authorizationUrlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ authorizationUrlChanged(self, QUrl) [signal] """
        pass

    def authorizeWithBrowser(self, QUrl): # real signature unknown; restored from __doc__
        """ authorizeWithBrowser(self, QUrl) [signal] """
        pass

    def callback(self): # real signature unknown; restored from __doc__
        """ callback(self) -> str """
        return ""

    def clientIdentifier(self): # real signature unknown; restored from __doc__
        """ clientIdentifier(self) -> str """
        return ""

    def clientIdentifierChanged(self, p_str): # real signature unknown; restored from __doc__
        """ clientIdentifierChanged(self, str) [signal] """
        pass

    def contentType(self): # real signature unknown; restored from __doc__
        """ contentType(self) -> QAbstractOAuth.ContentType """
        pass

    def contentTypeChanged(self, QAbstractOAuth_ContentType): # real signature unknown; restored from __doc__
        """ contentTypeChanged(self, QAbstractOAuth.ContentType) [signal] """
        pass

    def deleteResource(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ deleteResource(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def extraTokens(self): # real signature unknown; restored from __doc__
        """ extraTokens(self) -> Dict[str, Any] """
        return {}

    def extraTokensChanged(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ extraTokensChanged(self, Dict[str, Any]) [signal] """
        pass

    def finished(self, QNetworkReply): # real signature unknown; restored from __doc__
        """ finished(self, QNetworkReply) [signal] """
        pass

    def generateRandomString(self, p_int): # real signature unknown; restored from __doc__
        """ generateRandomString(int) -> QByteArray """
        pass

    def get(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ get(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def grant(self): # real signature unknown; restored from __doc__
        """ grant(self) """
        pass

    def granted(self): # real signature unknown; restored from __doc__
        """ granted(self) [signal] """
        pass

    def head(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ head(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def modifyParametersFunction(self): # real signature unknown; restored from __doc__
        """ modifyParametersFunction(self) -> Callable[..., None] """
        pass

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> QNetworkAccessManager """
        pass

    def post(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ post(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def put(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ put(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def replyDataReceived(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ replyDataReceived(self, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def replyHandler(self): # real signature unknown; restored from __doc__
        """ replyHandler(self) -> QAbstractOAuthReplyHandler """
        return QAbstractOAuthReplyHandler

    def requestFailed(self, QAbstractOAuth_Error): # real signature unknown; restored from __doc__
        """ requestFailed(self, QAbstractOAuth.Error) [signal] """
        pass

    def resourceOwnerAuthorization(self, QUrl, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ resourceOwnerAuthorization(self, QUrl, Dict[str, Any]) """
        pass

    def setAuthorizationUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setAuthorizationUrl(self, QUrl) """
        pass

    def setClientIdentifier(self, p_str): # real signature unknown; restored from __doc__
        """ setClientIdentifier(self, str) """
        pass

    def setContentType(self, QAbstractOAuth_ContentType): # real signature unknown; restored from __doc__
        """ setContentType(self, QAbstractOAuth.ContentType) """
        pass

    def setModifyParametersFunction(self, Callable, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setModifyParametersFunction(self, Callable[..., None]) """
        pass

    def setNetworkAccessManager(self, QNetworkAccessManager): # real signature unknown; restored from __doc__
        """ setNetworkAccessManager(self, QNetworkAccessManager) """
        pass

    def setReplyHandler(self, QAbstractOAuthReplyHandler): # real signature unknown; restored from __doc__
        """ setReplyHandler(self, QAbstractOAuthReplyHandler) """
        pass

    def setStatus(self, QAbstractOAuth_Status): # real signature unknown; restored from __doc__
        """ setStatus(self, QAbstractOAuth.Status) """
        pass

    def setToken(self, p_str): # real signature unknown; restored from __doc__
        """ setToken(self, str) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QAbstractOAuth.Status """
        pass

    def statusChanged(self, QAbstractOAuth_Status): # real signature unknown; restored from __doc__
        """ statusChanged(self, QAbstractOAuth.Status) [signal] """
        pass

    def token(self): # real signature unknown; restored from __doc__
        """ token(self) -> str """
        return ""

    def tokenChanged(self, p_str): # real signature unknown; restored from __doc__
        """ tokenChanged(self, str) [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass



class QAbstractOAuth2(QAbstractOAuth):
    """
    QAbstractOAuth2(parent: QObject = None)
    QAbstractOAuth2(QNetworkAccessManager, parent: QObject = None)
    """
    def authorizationCallbackReceived(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ authorizationCallbackReceived(self, Dict[str, Any]) [signal] """
        pass

    def clientIdentifierSharedKey(self): # real signature unknown; restored from __doc__
        """ clientIdentifierSharedKey(self) -> str """
        return ""

    def clientIdentifierSharedKeyChanged(self, p_str): # real signature unknown; restored from __doc__
        """ clientIdentifierSharedKeyChanged(self, str) [signal] """
        pass

    def createAuthenticatedUrl(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createAuthenticatedUrl(self, QUrl, parameters: Dict[str, Any] = {}) -> QUrl """
        pass

    def deleteResource(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ deleteResource(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def error(self, p_str, p_str_1, QUrl): # real signature unknown; restored from __doc__
        """ error(self, str, str, QUrl) [signal] """
        pass

    def expirationAt(self): # real signature unknown; restored from __doc__
        """ expirationAt(self) -> QDateTime """
        pass

    def expirationAtChanged(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ expirationAtChanged(self, Union[QDateTime, datetime.datetime]) [signal] """
        pass

    def get(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ get(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def head(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ head(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def post(self, QUrl, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        post(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply
        post(self, QUrl, Union[QByteArray, bytes, bytearray]) -> QNetworkReply
        post(self, QUrl, QHttpMultiPart) -> QNetworkReply
        """
        pass

    def put(self, QUrl, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        put(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply
        put(self, QUrl, Union[QByteArray, bytes, bytearray]) -> QNetworkReply
        put(self, QUrl, QHttpMultiPart) -> QNetworkReply
        """
        pass

    def refreshToken(self): # real signature unknown; restored from __doc__
        """ refreshToken(self) -> str """
        return ""

    def refreshTokenChanged(self, p_str): # real signature unknown; restored from __doc__
        """ refreshTokenChanged(self, str) [signal] """
        pass

    def responseType(self): # real signature unknown; restored from __doc__
        """ responseType(self) -> str """
        return ""

    def responseTypeChanged(self, p_str): # real signature unknown; restored from __doc__
        """ responseTypeChanged(self, str) [signal] """
        pass

    def scope(self): # real signature unknown; restored from __doc__
        """ scope(self) -> str """
        return ""

    def scopeChanged(self, p_str): # real signature unknown; restored from __doc__
        """ scopeChanged(self, str) [signal] """
        pass

    def setClientIdentifierSharedKey(self, p_str): # real signature unknown; restored from __doc__
        """ setClientIdentifierSharedKey(self, str) """
        pass

    def setRefreshToken(self, p_str): # real signature unknown; restored from __doc__
        """ setRefreshToken(self, str) """
        pass

    def setResponseType(self, p_str): # real signature unknown; restored from __doc__
        """ setResponseType(self, str) """
        pass

    def setScope(self, p_str): # real signature unknown; restored from __doc__
        """ setScope(self, str) """
        pass

    def setState(self, p_str): # real signature unknown; restored from __doc__
        """ setState(self, str) """
        pass

    def setUserAgent(self, p_str): # real signature unknown; restored from __doc__
        """ setUserAgent(self, str) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> str """
        return ""

    def stateChanged(self, p_str): # real signature unknown; restored from __doc__
        """ stateChanged(self, str) [signal] """
        pass

    def userAgent(self): # real signature unknown; restored from __doc__
        """ userAgent(self) -> str """
        return ""

    def userAgentChanged(self, p_str): # real signature unknown; restored from __doc__
        """ userAgentChanged(self, str) [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QAbstractOAuthReplyHandler(__PyQt5_QtCore.QObject):
    """ QAbstractOAuthReplyHandler(parent: QObject = None) """
    def callback(self): # real signature unknown; restored from __doc__
        """ callback(self) -> str """
        return ""

    def callbackDataReceived(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ callbackDataReceived(self, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def callbackReceived(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ callbackReceived(self, Dict[str, Any]) [signal] """
        pass

    def networkReplyFinished(self, QNetworkReply): # real signature unknown; restored from __doc__
        """ networkReplyFinished(self, QNetworkReply) """
        pass

    def replyDataReceived(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ replyDataReceived(self, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def tokensReceived(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ tokensReceived(self, Dict[str, Any]) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QOAuth1(QAbstractOAuth):
    """
    QOAuth1(parent: QObject = None)
    QOAuth1(QNetworkAccessManager, parent: QObject = None)
    QOAuth1(str, str, QNetworkAccessManager, parent: QObject = None)
    """
    def clientCredentials(self): # real signature unknown; restored from __doc__
        """ clientCredentials(self) -> Tuple[str, str] """
        pass

    def clientSharedSecret(self): # real signature unknown; restored from __doc__
        """ clientSharedSecret(self) -> str """
        return ""

    def clientSharedSecretChanged(self, p_str): # real signature unknown; restored from __doc__
        """ clientSharedSecretChanged(self, str) [signal] """
        pass

    def continueGrantWithVerifier(self, p_str): # real signature unknown; restored from __doc__
        """ continueGrantWithVerifier(self, str) """
        pass

    def deleteResource(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ deleteResource(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def generateAuthorizationHeader(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ generateAuthorizationHeader(Dict[str, Any]) -> QByteArray """
        pass

    def get(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ get(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def grant(self): # real signature unknown; restored from __doc__
        """ grant(self) """
        pass

    def head(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ head(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def nonce(self): # real signature unknown; restored from __doc__
        """ nonce() -> QByteArray """
        pass

    def post(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ post(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def put(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ put(self, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def requestTemporaryCredentials(self, QNetworkAccessManager_Operation, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ requestTemporaryCredentials(self, QNetworkAccessManager.Operation, QUrl, parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def requestTokenCredentials(self, QNetworkAccessManager_Operation, QUrl, Tuple, p_str=None, p_str=None_1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ requestTokenCredentials(self, QNetworkAccessManager.Operation, QUrl, Tuple[str, str], parameters: Dict[str, Any] = {}) -> QNetworkReply """
        pass

    def setClientCredentials(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setClientCredentials(self, Tuple[str, str])
        setClientCredentials(self, str, str)
        """
        pass

    def setClientSharedSecret(self, p_str): # real signature unknown; restored from __doc__
        """ setClientSharedSecret(self, str) """
        pass

    def setSignatureMethod(self, QOAuth1_SignatureMethod): # real signature unknown; restored from __doc__
        """ setSignatureMethod(self, QOAuth1.SignatureMethod) """
        pass

    def setTemporaryCredentialsUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setTemporaryCredentialsUrl(self, QUrl) """
        pass

    def setTokenCredentials(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setTokenCredentials(self, Tuple[str, str])
        setTokenCredentials(self, str, str)
        """
        pass

    def setTokenCredentialsUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setTokenCredentialsUrl(self, QUrl) """
        pass

    def setTokenSecret(self, p_str): # real signature unknown; restored from __doc__
        """ setTokenSecret(self, str) """
        pass

    def setup(self, QNetworkRequest, Dict, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setup(self, QNetworkRequest, Dict[str, Any], QNetworkAccessManager.Operation) """
        pass

    def signatureMethod(self): # real signature unknown; restored from __doc__
        """ signatureMethod(self) -> QOAuth1.SignatureMethod """
        pass

    def signatureMethodChanged(self, QOAuth1_SignatureMethod): # real signature unknown; restored from __doc__
        """ signatureMethodChanged(self, QOAuth1.SignatureMethod) [signal] """
        pass

    def temporaryCredentialsUrl(self): # real signature unknown; restored from __doc__
        """ temporaryCredentialsUrl(self) -> QUrl """
        pass

    def temporaryCredentialsUrlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ temporaryCredentialsUrlChanged(self, QUrl) [signal] """
        pass

    def tokenCredentials(self): # real signature unknown; restored from __doc__
        """ tokenCredentials(self) -> Tuple[str, str] """
        pass

    def tokenCredentialsUrl(self): # real signature unknown; restored from __doc__
        """ tokenCredentialsUrl(self) -> QUrl """
        pass

    def tokenCredentialsUrlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ tokenCredentialsUrlChanged(self, QUrl) [signal] """
        pass

    def tokenSecret(self): # real signature unknown; restored from __doc__
        """ tokenSecret(self) -> str """
        return ""

    def tokenSecretChanged(self, p_str): # real signature unknown; restored from __doc__
        """ tokenSecretChanged(self, str) [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass



class QOAuth1Signature(__sip.simplewrapper):
    """
    QOAuth1Signature(url: QUrl = QUrl(), method: QOAuth1Signature.HttpRequestMethod = QOAuth1Signature.HttpRequestMethod.Post, parameters: Dict[str, Any] = {})
    QOAuth1Signature(QUrl, str, str, method: QOAuth1Signature.HttpRequestMethod = QOAuth1Signature.HttpRequestMethod.Post, parameters: Dict[str, Any] = {})
    QOAuth1Signature(QOAuth1Signature)
    """
    def addRequestBody(self, QUrlQuery): # real signature unknown; restored from __doc__
        """ addRequestBody(self, QUrlQuery) """
        pass

    def clientSharedKey(self): # real signature unknown; restored from __doc__
        """ clientSharedKey(self) -> str """
        return ""

    def hmacSha1(self): # real signature unknown; restored from __doc__
        """ hmacSha1(self) -> QByteArray """
        pass

    def httpRequestMethod(self): # real signature unknown; restored from __doc__
        """ httpRequestMethod(self) -> QOAuth1Signature.HttpRequestMethod """
        pass

    def insert(self, p_str, Any): # real signature unknown; restored from __doc__
        """ insert(self, str, Any) """
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """ keys(self) -> List[str] """
        return []

    def parameters(self): # real signature unknown; restored from __doc__
        """ parameters(self) -> Dict[str, Any] """
        return {}

    def plainText(self, p_str=None, p_str_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        plainText(self) -> QByteArray
        plainText(str, str) -> QByteArray
        """
        pass

    def rsaSha1(self): # real signature unknown; restored from __doc__
        """ rsaSha1(self) -> QByteArray """
        pass

    def setClientSharedKey(self, p_str): # real signature unknown; restored from __doc__
        """ setClientSharedKey(self, str) """
        pass

    def setHttpRequestMethod(self, QOAuth1Signature_HttpRequestMethod): # real signature unknown; restored from __doc__
        """ setHttpRequestMethod(self, QOAuth1Signature.HttpRequestMethod) """
        pass

    def setParameters(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setParameters(self, Dict[str, Any]) """
        pass

    def setTokenSecret(self, p_str): # real signature unknown; restored from __doc__
        """ setTokenSecret(self, str) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def swap(self, QOAuth1Signature): # real signature unknown; restored from __doc__
        """ swap(self, QOAuth1Signature) """
        pass

    def take(self, p_str): # real signature unknown; restored from __doc__
        """ take(self, str) -> Any """
        pass

    def tokenSecret(self): # real signature unknown; restored from __doc__
        """ tokenSecret(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def value(self, p_str, defaultValue=None): # real signature unknown; restored from __doc__
        """ value(self, str, defaultValue: Any = None) -> Any """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




class QOAuth2AuthorizationCodeFlow(QAbstractOAuth2):
    """
    QOAuth2AuthorizationCodeFlow(parent: QObject = None)
    QOAuth2AuthorizationCodeFlow(QNetworkAccessManager, parent: QObject = None)
    QOAuth2AuthorizationCodeFlow(str, QNetworkAccessManager, parent: QObject = None)
    QOAuth2AuthorizationCodeFlow(QUrl, QUrl, QNetworkAccessManager, parent: QObject = None)
    QOAuth2AuthorizationCodeFlow(str, QUrl, QUrl, QNetworkAccessManager, parent: QObject = None)
    """
    def accessTokenUrl(self): # real signature unknown; restored from __doc__
        """ accessTokenUrl(self) -> QUrl """
        pass

    def accessTokenUrlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ accessTokenUrlChanged(self, QUrl) [signal] """
        pass

    def buildAuthenticateUrl(self, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ buildAuthenticateUrl(self, parameters: Dict[str, Any] = {}) -> QUrl """
        pass

    def grant(self): # real signature unknown; restored from __doc__
        """ grant(self) """
        pass

    def refreshAccessToken(self): # real signature unknown; restored from __doc__
        """ refreshAccessToken(self) """
        pass

    def requestAccessToken(self, p_str): # real signature unknown; restored from __doc__
        """ requestAccessToken(self, str) """
        pass

    def resourceOwnerAuthorization(self, QUrl, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ resourceOwnerAuthorization(self, QUrl, parameters: Dict[str, Any] = {}) """
        pass

    def setAccessTokenUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setAccessTokenUrl(self, QUrl) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QOAuthOobReplyHandler(QAbstractOAuthReplyHandler):
    """ QOAuthOobReplyHandler(parent: QObject = None) """
    def callback(self): # real signature unknown; restored from __doc__
        """ callback(self) -> str """
        return ""

    def networkReplyFinished(self, QNetworkReply): # real signature unknown; restored from __doc__
        """ networkReplyFinished(self, QNetworkReply) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QOAuthHttpServerReplyHandler(QOAuthOobReplyHandler):
    """
    QOAuthHttpServerReplyHandler(parent: QObject = None)
    QOAuthHttpServerReplyHandler(int, parent: QObject = None)
    QOAuthHttpServerReplyHandler(Union[QHostAddress, QHostAddress.SpecialAddress], int, parent: QObject = None)
    """
    def callback(self): # real signature unknown; restored from __doc__
        """ callback(self) -> str """
        return ""

    def callbackPath(self): # real signature unknown; restored from __doc__
        """ callbackPath(self) -> str """
        return ""

    def callbackText(self): # real signature unknown; restored from __doc__
        """ callbackText(self) -> str """
        return ""

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def listen(self, address, QHostAddress=None, QHostAddress_SpecialAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ listen(self, address: Union[QHostAddress, QHostAddress.SpecialAddress] = QHostAddress.SpecialAddress.Any, port: int = 0) -> bool """
        pass

    def port(self): # real signature unknown; restored from __doc__
        """ port(self) -> int """
        return 0

    def setCallbackPath(self, p_str): # real signature unknown; restored from __doc__
        """ setCallbackPath(self, str) """
        pass

    def setCallbackText(self, p_str): # real signature unknown; restored from __doc__
        """ setCallbackText(self, str) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


# variables with complex values



