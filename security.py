from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash_senha(senha_pura: str) -> str:
    """Transformar a senha comum em uma hash seguro para salvar no banco."""
    return pwd_context.hash(senha_pura)

def verificar_senha(senha_pura: str, senha_criptografada: str) -> bool:
    """Verifica se a senha digitada corresponde ao hash do banco (usado no login)."""
    return pwd_context.verify(senha_pura, senha_criptografada)